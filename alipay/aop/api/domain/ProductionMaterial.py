#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductionMaterial(object):

    def __init__(self):
        self._coil_link_url = None
        self._desk_no = None
        self._position_name = None
        self._print_qr_code_url = None
        self._variable_ext_tr_info = None

    @property
    def coil_link_url(self):
        return self._coil_link_url

    @coil_link_url.setter
    def coil_link_url(self, value):
        self._coil_link_url = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
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
    def variable_ext_tr_info(self):
        return self._variable_ext_tr_info

    @variable_ext_tr_info.setter
    def variable_ext_tr_info(self, value):
        self._variable_ext_tr_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.coil_link_url:
            if hasattr(self.coil_link_url, 'to_alipay_dict'):
                params['coil_link_url'] = self.coil_link_url.to_alipay_dict()
            else:
                params['coil_link_url'] = self.coil_link_url
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
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
        if self.variable_ext_tr_info:
            if hasattr(self.variable_ext_tr_info, 'to_alipay_dict'):
                params['variable_ext_tr_info'] = self.variable_ext_tr_info.to_alipay_dict()
            else:
                params['variable_ext_tr_info'] = self.variable_ext_tr_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductionMaterial()
        if 'coil_link_url' in d:
            o.coil_link_url = d['coil_link_url']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'position_name' in d:
            o.position_name = d['position_name']
        if 'print_qr_code_url' in d:
            o.print_qr_code_url = d['print_qr_code_url']
        if 'variable_ext_tr_info' in d:
            o.variable_ext_tr_info = d['variable_ext_tr_info']
        return o


