#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NcoilopenAddressInfo import NcoilopenAddressInfo
from alipay.aop.api.domain.ExtAttributeInfo import ExtAttributeInfo


class AlipayOpenSpNcoilopenTempAddModel(object):

    def __init__(self):
        self._address_info_map = None
        self._coil_link_url = None
        self._coil_no = None
        self._coil_total = None
        self._desk_no = None
        self._ext_attr_list = None
        self._group_no = None
        self._position_name = None
        self._print_qr_code_url = None
        self._reference_id = None

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
    def position_name(self):
        return self._position_name

    @position_name.setter
    def position_name(self, value):
        self._position_name = value
    @property
    def print_qr_code_url(self):
        return self._print_qr_code_url

    @print_qr_code_url.setter
    def print_qr_code_url(self, value):
        self._print_qr_code_url = value
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info_map:
            if hasattr(self.address_info_map, 'to_alipay_dict'):
                params['address_info_map'] = self.address_info_map.to_alipay_dict()
            else:
                params['address_info_map'] = self.address_info_map
        if self.coil_link_url:
            if hasattr(self.coil_link_url, 'to_alipay_dict'):
                params['coil_link_url'] = self.coil_link_url.to_alipay_dict()
            else:
                params['coil_link_url'] = self.coil_link_url
        if self.coil_no:
            if hasattr(self.coil_no, 'to_alipay_dict'):
                params['coil_no'] = self.coil_no.to_alipay_dict()
            else:
                params['coil_no'] = self.coil_no
        if self.coil_total:
            if hasattr(self.coil_total, 'to_alipay_dict'):
                params['coil_total'] = self.coil_total.to_alipay_dict()
            else:
                params['coil_total'] = self.coil_total
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.ext_attr_list:
            if isinstance(self.ext_attr_list, list):
                for i in range(0, len(self.ext_attr_list)):
                    element = self.ext_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_attr_list, 'to_alipay_dict'):
                params['ext_attr_list'] = self.ext_attr_list.to_alipay_dict()
            else:
                params['ext_attr_list'] = self.ext_attr_list
        if self.group_no:
            if hasattr(self.group_no, 'to_alipay_dict'):
                params['group_no'] = self.group_no.to_alipay_dict()
            else:
                params['group_no'] = self.group_no
        if self.position_name:
            if hasattr(self.position_name, 'to_alipay_dict'):
                params['position_name'] = self.position_name.to_alipay_dict()
            else:
                params['position_name'] = self.position_name
        if self.print_qr_code_url:
            if hasattr(self.print_qr_code_url, 'to_alipay_dict'):
                params['print_qr_code_url'] = self.print_qr_code_url.to_alipay_dict()
            else:
                params['print_qr_code_url'] = self.print_qr_code_url
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNcoilopenTempAddModel()
        if 'address_info_map' in d:
            o.address_info_map = d['address_info_map']
        if 'coil_link_url' in d:
            o.coil_link_url = d['coil_link_url']
        if 'coil_no' in d:
            o.coil_no = d['coil_no']
        if 'coil_total' in d:
            o.coil_total = d['coil_total']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'ext_attr_list' in d:
            o.ext_attr_list = d['ext_attr_list']
        if 'group_no' in d:
            o.group_no = d['group_no']
        if 'position_name' in d:
            o.position_name = d['position_name']
        if 'print_qr_code_url' in d:
            o.print_qr_code_url = d['print_qr_code_url']
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        return o


