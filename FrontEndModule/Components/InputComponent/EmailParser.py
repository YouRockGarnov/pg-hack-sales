import re

class EmailParser:
    def parse_email(self, email):
        march = re.search('<div>[\s|\S]*</div>', email)
        cells = march.group(0).replace('<div>', '')
        cells = cells.split('</div>')
        cells = filter(lambda x: x != '', cells)

        filtered_cells = []

        norm_cells = list()
        cells = list(cells)
        for item in cells:
            if not 'xa' in item:
                norm_cells.append(item)

        cells = norm_cells
        for item in cells:
            #print(list(cells))

            item = item.split(':')
            item[0] = item[0].replace(' ', '')
            item[1] = item[1].replace(' ', '')

            filtered_cells.append(item)

        return self.prepare_for_csv(filtered_cells)

    def prepare_for_csv(self, cells):
        ans = []
        ziped_rows = zip(cells[0::3], cells[1::3], cells[2::3])
        for three in ziped_rows:
            row = dict()

            for pair in three:
                row[pair[0]] = pair[1]

            ans.append(row)

        return ans