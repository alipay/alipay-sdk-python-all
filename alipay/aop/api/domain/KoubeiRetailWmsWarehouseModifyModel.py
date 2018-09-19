#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsWarehouseModifyModel(object):

    def __init__(self):
        self._ext_info = None
        self._safety_inventory_switch = None
        self._warehouse_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def safety_inventory_switch(self):
        return self._safety_inventory_switch

    @safety_inventory_switch.setter
    def safety_inventory_switch(self, value):
        self._safety_inventory_switch = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.safety_inventory_switch:
            if hasattr(self.safety_inventory_switch, 'to_alipay_dict'):
                params['safety_inventory_switch'] = self.safety_inventory_switch.to_alipay_dict()
            else:
                params['safety_inventory_switch'] = self.safety_inventory_switch
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsWarehouseModifyModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'safety_inventory_switch' in d:
            o.safety_inventory_switch = d['safety_inventory_switch']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


