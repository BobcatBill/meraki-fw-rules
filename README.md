Python script to pull down all the Meraki MX firewall rules in an organization.  Supply the API key and Org ID.  Script will:

1. Pull down all network IDs from the organzation ID that was supplied
2. Parse the list of network IDs and pull the firewall rules on each MX firewall
3. Put each ruleset in it's own filename under the naming convention "NetworkName.csv"
4. Encapsulates each rule with single quotes so that commas contained within each rule field is parsed correctly by CSV reader

Script requires meraki python module and only works on network type of "appliance" or "combined" (Systems Manager and Wireless are skipped).

