# Lauren L Rodgers, Michael N Weedon, William E Henley, Andrew T Hattersley, Beverley M Shields, 2024.

import sys, csv, re

codes = [{"code":"42W1.00","system":"readv2"},{"code":"42c3.00","system":"readv2"},{"code":"42W..00","system":"readv2"},{"code":"42c2.00","system":"readv2"},{"code":"42W..11","system":"readv2"},{"code":"42W2.00","system":"readv2"},{"code":"42W4.00","system":"readv2"},{"code":"66Ae.00","system":"readv2"},{"code":"42c1.00","system":"readv2"},{"code":"44TB.00","system":"readv2"},{"code":"42c..00","system":"readv2"},{"code":"42W..12","system":"readv2"},{"code":"44TL.00","system":"readv2"},{"code":"66Ae000","system":"readv2"},{"code":"42W5.00","system":"readv2"},{"code":"42c0.00","system":"readv2"},{"code":"42W3.00","system":"readv2"},{"code":"42WZ.00","system":"readv2"},{"code":"44TC.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('type-2-diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["type-2-diabetes-hba1c-test-codes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["type-2-diabetes-hba1c-test-codes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["type-2-diabetes-hba1c-test-codes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
