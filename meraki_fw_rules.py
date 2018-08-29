import csv
import meraki
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = ''
org_id = ''

logger.info("Collecting Network List")
network_list = meraki.getnetworklist(api_key,org_id,suppressprint=True)
logger.info("Finished Network List Collection")
for site_list in network_list:
        if site_list['type'] == "combined" or site_list['type'] == "appliance" :
                filename = site_list['name']
                filename = "output/" + filename + ".csv"
                output_file = open(filename, mode='w')
                csv_writer = csv.writer(output_file, quotechar='"', delimiter=';', quoting=csv.QUOTE_NONE, skipinitialspace=True)
                header_row_text = "'Comment','Policy','Protocol','Source Port','Source CIDR','Destination Port','Destination CIDR','Log Enabled'"
                csv_writer.writerow([header_row_text])
                net_id = site_list['id']
                logger.info("Collecting rules from site")
                fw_rules = meraki.getmxl3fwrules(api_key,net_id,suppressprint=True)
                for rule in fw_rules:
                        csv_row = "'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'".format(rule['comment'],rule['policy'],rule['protocol'],rule['srcPort'],rule['srcCidr'],rule['destPort'],rule['destCidr'],rule['syslogEnabled'])
                        csv_writer.writerow([csv_row])
                csv_writer.writerow([csv_row])
                output_file.close()
