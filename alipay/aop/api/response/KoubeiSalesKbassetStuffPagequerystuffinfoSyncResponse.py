#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StuffInfo import StuffInfo


class KoubeiSalesKbassetStuffPagequerystuffinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffPagequerystuffinfoSyncResponse, self).__init__()
        self._error_code = None
        self._error_desc = None
        self._ext_info = None
        self._page_no = None
        self._page_size = None
        self._stuff_infos = None
        self._success = None
        self._total_count = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def stuff_infos(self):
        return self._stuff_infos

    @stuff_infos.setter
    def stuff_infos(self, value):
        if isinstance(value, list):
            self._stuff_infos = list()
            for i in value:
                if isinstance(i, StuffInfo):
                    self._stuff_infos.append(i)
                else:
                    self._stuff_infos.append(StuffInfo.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffPagequerystuffinfoSyncResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_desc' in response:
            self.error_desc = response['error_desc']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'stuff_infos' in response:
            self.stuff_infos = response['stuff_infos']
        if 'success' in response:
            self.success = response['success']
        if 'total_count' in response:
            self.total_count = response['total_count']
