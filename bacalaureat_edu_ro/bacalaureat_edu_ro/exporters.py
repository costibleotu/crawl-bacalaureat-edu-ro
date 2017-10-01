from bacalaureat_edu_ro import settings
from scrapy.exporters import CsvItemExporter
import csv

class bacalaureatCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.CSV_DELIMITER
        quotechar = settings.CSV_QUOTECHAR
        kwargs['delimiter'] = delimiter
        kwargs['quotechar'] = quotechar
        kwargs['quoting'] = csv.QUOTE_ALL

        fields_to_export = settings.CSV_FIELDS_TO_EXPORT
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export

        super(bacalaureatCsvItemExporter, self).__init__(*args, **kwargs)

    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                self.fields_to_export = item.fields.keys()
            self.csv_writer.writerow([field for field in self.fields_to_export])