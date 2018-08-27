#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupplierReport import SupplierReport
from alipay.aop.api.domain.SupplierReportDetail import SupplierReportDetail


class KoubeiRetailWmsSupplierreportdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsSupplierreportdetailQueryResponse, self).__init__()
        self._supplier_report = None
        self._supplier_report_details = None

    @property
    def supplier_report(self):
        return self._supplier_report

    @supplier_report.setter
    def supplier_report(self, value):
        if isinstance(value, SupplierReport):
            self._supplier_report = value
        else:
            self._supplier_report = SupplierReport.from_alipay_dict(value)
    @property
    def supplier_report_details(self):
        return self._supplier_report_details

    @supplier_report_details.setter
    def supplier_report_details(self, value):
        if isinstance(value, list):
            self._supplier_report_details = list()
            for i in value:
                if isinstance(i, SupplierReportDetail):
                    self._supplier_report_details.append(i)
                else:
                    self._supplier_report_details.append(SupplierReportDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsSupplierreportdetailQueryResponse, self).parse_response_content(response_content)
        if 'supplier_report' in response:
            self.supplier_report = response['supplier_report']
        if 'supplier_report_details' in response:
            self.supplier_report_details = response['supplier_report_details']
