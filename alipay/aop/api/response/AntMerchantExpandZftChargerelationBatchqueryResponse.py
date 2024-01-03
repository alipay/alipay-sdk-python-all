#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChargeRelationInfo import ChargeRelationInfo


class AntMerchantExpandZftChargerelationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandZftChargerelationBatchqueryResponse, self).__init__()
        self._charge_relation_infos = None
        self._page_num = None
        self._page_size = None
        self._total_pages = None
        self._total_size = None

    @property
    def charge_relation_infos(self):
        return self._charge_relation_infos

    @charge_relation_infos.setter
    def charge_relation_infos(self, value):
        if isinstance(value, list):
            self._charge_relation_infos = list()
            for i in value:
                if isinstance(i, ChargeRelationInfo):
                    self._charge_relation_infos.append(i)
                else:
                    self._charge_relation_infos.append(ChargeRelationInfo.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandZftChargerelationBatchqueryResponse, self).parse_response_content(response_content)
        if 'charge_relation_infos' in response:
            self.charge_relation_infos = response['charge_relation_infos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
