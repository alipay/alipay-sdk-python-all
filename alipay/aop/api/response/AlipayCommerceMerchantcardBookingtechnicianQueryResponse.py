#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AxfBookingTechnicianInfo import AxfBookingTechnicianInfo


class AlipayCommerceMerchantcardBookingtechnicianQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardBookingtechnicianQueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._technician_infos = None
        self._total = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def technician_infos(self):
        return self._technician_infos

    @technician_infos.setter
    def technician_infos(self, value):
        if isinstance(value, list):
            self._technician_infos = list()
            for i in value:
                if isinstance(i, AxfBookingTechnicianInfo):
                    self._technician_infos.append(i)
                else:
                    self._technician_infos.append(AxfBookingTechnicianInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardBookingtechnicianQueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'technician_infos' in response:
            self.technician_infos = response['technician_infos']
        if 'total' in response:
            self.total = response['total']
