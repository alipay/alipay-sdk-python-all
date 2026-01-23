#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AxfBookingServiceInfo import AxfBookingServiceInfo


class AlipayCommerceMerchantcardBookingserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardBookingserviceQueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._service_infos = None
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
    def service_infos(self):
        return self._service_infos

    @service_infos.setter
    def service_infos(self, value):
        if isinstance(value, list):
            self._service_infos = list()
            for i in value:
                if isinstance(i, AxfBookingServiceInfo):
                    self._service_infos.append(i)
                else:
                    self._service_infos.append(AxfBookingServiceInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardBookingserviceQueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'service_infos' in response:
            self.service_infos = response['service_infos']
        if 'total' in response:
            self.total = response['total']
