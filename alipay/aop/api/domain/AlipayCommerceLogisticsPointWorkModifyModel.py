#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessAddress import BusinessAddress
from alipay.aop.api.domain.BusinessAddress import BusinessAddress


class AlipayCommerceLogisticsPointWorkModifyModel(object):

    def __init__(self):
        self._desc = None
        self._logistics_nfc_id = None
        self._new_place_id = None
        self._new_place_name = None
        self._new_point_id = None
        self._new_point_name = None
        self._nfc_status = None
        self._old_place_id = None
        self._old_point_id = None
        self._operator_type = None
        self._out_place_id = None
        self._work_place_address = None
        self._work_point_address = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def logistics_nfc_id(self):
        return self._logistics_nfc_id

    @logistics_nfc_id.setter
    def logistics_nfc_id(self, value):
        self._logistics_nfc_id = value
    @property
    def new_place_id(self):
        return self._new_place_id

    @new_place_id.setter
    def new_place_id(self, value):
        self._new_place_id = value
    @property
    def new_place_name(self):
        return self._new_place_name

    @new_place_name.setter
    def new_place_name(self, value):
        self._new_place_name = value
    @property
    def new_point_id(self):
        return self._new_point_id

    @new_point_id.setter
    def new_point_id(self, value):
        self._new_point_id = value
    @property
    def new_point_name(self):
        return self._new_point_name

    @new_point_name.setter
    def new_point_name(self, value):
        self._new_point_name = value
    @property
    def nfc_status(self):
        return self._nfc_status

    @nfc_status.setter
    def nfc_status(self, value):
        self._nfc_status = value
    @property
    def old_place_id(self):
        return self._old_place_id

    @old_place_id.setter
    def old_place_id(self, value):
        self._old_place_id = value
    @property
    def old_point_id(self):
        return self._old_point_id

    @old_point_id.setter
    def old_point_id(self, value):
        self._old_point_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def out_place_id(self):
        return self._out_place_id

    @out_place_id.setter
    def out_place_id(self, value):
        self._out_place_id = value
    @property
    def work_place_address(self):
        return self._work_place_address

    @work_place_address.setter
    def work_place_address(self, value):
        if isinstance(value, BusinessAddress):
            self._work_place_address = value
        else:
            self._work_place_address = BusinessAddress.from_alipay_dict(value)
    @property
    def work_point_address(self):
        return self._work_point_address

    @work_point_address.setter
    def work_point_address(self, value):
        if isinstance(value, BusinessAddress):
            self._work_point_address = value
        else:
            self._work_point_address = BusinessAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.logistics_nfc_id:
            if hasattr(self.logistics_nfc_id, 'to_alipay_dict'):
                params['logistics_nfc_id'] = self.logistics_nfc_id.to_alipay_dict()
            else:
                params['logistics_nfc_id'] = self.logistics_nfc_id
        if self.new_place_id:
            if hasattr(self.new_place_id, 'to_alipay_dict'):
                params['new_place_id'] = self.new_place_id.to_alipay_dict()
            else:
                params['new_place_id'] = self.new_place_id
        if self.new_place_name:
            if hasattr(self.new_place_name, 'to_alipay_dict'):
                params['new_place_name'] = self.new_place_name.to_alipay_dict()
            else:
                params['new_place_name'] = self.new_place_name
        if self.new_point_id:
            if hasattr(self.new_point_id, 'to_alipay_dict'):
                params['new_point_id'] = self.new_point_id.to_alipay_dict()
            else:
                params['new_point_id'] = self.new_point_id
        if self.new_point_name:
            if hasattr(self.new_point_name, 'to_alipay_dict'):
                params['new_point_name'] = self.new_point_name.to_alipay_dict()
            else:
                params['new_point_name'] = self.new_point_name
        if self.nfc_status:
            if hasattr(self.nfc_status, 'to_alipay_dict'):
                params['nfc_status'] = self.nfc_status.to_alipay_dict()
            else:
                params['nfc_status'] = self.nfc_status
        if self.old_place_id:
            if hasattr(self.old_place_id, 'to_alipay_dict'):
                params['old_place_id'] = self.old_place_id.to_alipay_dict()
            else:
                params['old_place_id'] = self.old_place_id
        if self.old_point_id:
            if hasattr(self.old_point_id, 'to_alipay_dict'):
                params['old_point_id'] = self.old_point_id.to_alipay_dict()
            else:
                params['old_point_id'] = self.old_point_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.out_place_id:
            if hasattr(self.out_place_id, 'to_alipay_dict'):
                params['out_place_id'] = self.out_place_id.to_alipay_dict()
            else:
                params['out_place_id'] = self.out_place_id
        if self.work_place_address:
            if hasattr(self.work_place_address, 'to_alipay_dict'):
                params['work_place_address'] = self.work_place_address.to_alipay_dict()
            else:
                params['work_place_address'] = self.work_place_address
        if self.work_point_address:
            if hasattr(self.work_point_address, 'to_alipay_dict'):
                params['work_point_address'] = self.work_point_address.to_alipay_dict()
            else:
                params['work_point_address'] = self.work_point_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsPointWorkModifyModel()
        if 'desc' in d:
            o.desc = d['desc']
        if 'logistics_nfc_id' in d:
            o.logistics_nfc_id = d['logistics_nfc_id']
        if 'new_place_id' in d:
            o.new_place_id = d['new_place_id']
        if 'new_place_name' in d:
            o.new_place_name = d['new_place_name']
        if 'new_point_id' in d:
            o.new_point_id = d['new_point_id']
        if 'new_point_name' in d:
            o.new_point_name = d['new_point_name']
        if 'nfc_status' in d:
            o.nfc_status = d['nfc_status']
        if 'old_place_id' in d:
            o.old_place_id = d['old_place_id']
        if 'old_point_id' in d:
            o.old_point_id = d['old_point_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'out_place_id' in d:
            o.out_place_id = d['out_place_id']
        if 'work_place_address' in d:
            o.work_place_address = d['work_place_address']
        if 'work_point_address' in d:
            o.work_point_address = d['work_point_address']
        return o


