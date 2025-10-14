#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NcoilopenAddressInfo import NcoilopenAddressInfo
from alipay.aop.api.domain.ExtAttributeInfo import ExtAttributeInfo


class AlipayOpenSpNcoilopenTempQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenTempQueryResponse, self).__init__()
        self._address_info_map = None
        self._biz_id = None
        self._coil_link_url = None
        self._coil_no = None
        self._coil_total = None
        self._desk_no = None
        self._ext_attr_list = None
        self._group_no = None
        self._print_qr_code_url = None
        self._record_id = None

    @property
    def address_info_map(self):
        return self._address_info_map

    @address_info_map.setter
    def address_info_map(self, value):
        if isinstance(value, NcoilopenAddressInfo):
            self._address_info_map = value
        else:
            self._address_info_map = NcoilopenAddressInfo.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def coil_link_url(self):
        return self._coil_link_url

    @coil_link_url.setter
    def coil_link_url(self, value):
        self._coil_link_url = value
    @property
    def coil_no(self):
        return self._coil_no

    @coil_no.setter
    def coil_no(self, value):
        self._coil_no = value
    @property
    def coil_total(self):
        return self._coil_total

    @coil_total.setter
    def coil_total(self, value):
        self._coil_total = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def ext_attr_list(self):
        return self._ext_attr_list

    @ext_attr_list.setter
    def ext_attr_list(self, value):
        if isinstance(value, list):
            self._ext_attr_list = list()
            for i in value:
                if isinstance(i, ExtAttributeInfo):
                    self._ext_attr_list.append(i)
                else:
                    self._ext_attr_list.append(ExtAttributeInfo.from_alipay_dict(i))
    @property
    def group_no(self):
        return self._group_no

    @group_no.setter
    def group_no(self, value):
        self._group_no = value
    @property
    def print_qr_code_url(self):
        return self._print_qr_code_url

    @print_qr_code_url.setter
    def print_qr_code_url(self, value):
        self._print_qr_code_url = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenTempQueryResponse, self).parse_response_content(response_content)
        if 'address_info_map' in response:
            self.address_info_map = response['address_info_map']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'coil_link_url' in response:
            self.coil_link_url = response['coil_link_url']
        if 'coil_no' in response:
            self.coil_no = response['coil_no']
        if 'coil_total' in response:
            self.coil_total = response['coil_total']
        if 'desk_no' in response:
            self.desk_no = response['desk_no']
        if 'ext_attr_list' in response:
            self.ext_attr_list = response['ext_attr_list']
        if 'group_no' in response:
            self.group_no = response['group_no']
        if 'print_qr_code_url' in response:
            self.print_qr_code_url = response['print_qr_code_url']
        if 'record_id' in response:
            self.record_id = response['record_id']
