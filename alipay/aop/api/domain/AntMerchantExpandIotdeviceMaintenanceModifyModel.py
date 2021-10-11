#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIotdeviceMaintenanceModifyModel(object):

    def __init__(self):
        self._gmt_created = None
        self._gmt_modified = None
        self._install_order_id = None
        self._memo = None
        self._new_device_sn = None
        self._old_device_sn = None
        self._order_id = None
        self._problem_type = None
        self._repair_mobile = None
        self._repair_name = None
        self._shop_contact_mobile = None
        self._shop_contact_name = None
        self._shop_name = None
        self._signed_alipay_id = None
        self._supplier_sn = None

    @property
    def gmt_created(self):
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, value):
        self._gmt_created = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def install_order_id(self):
        return self._install_order_id

    @install_order_id.setter
    def install_order_id(self, value):
        self._install_order_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def new_device_sn(self):
        return self._new_device_sn

    @new_device_sn.setter
    def new_device_sn(self, value):
        self._new_device_sn = value
    @property
    def old_device_sn(self):
        return self._old_device_sn

    @old_device_sn.setter
    def old_device_sn(self, value):
        self._old_device_sn = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def problem_type(self):
        return self._problem_type

    @problem_type.setter
    def problem_type(self, value):
        self._problem_type = value
    @property
    def repair_mobile(self):
        return self._repair_mobile

    @repair_mobile.setter
    def repair_mobile(self, value):
        self._repair_mobile = value
    @property
    def repair_name(self):
        return self._repair_name

    @repair_name.setter
    def repair_name(self, value):
        self._repair_name = value
    @property
    def shop_contact_mobile(self):
        return self._shop_contact_mobile

    @shop_contact_mobile.setter
    def shop_contact_mobile(self, value):
        self._shop_contact_mobile = value
    @property
    def shop_contact_name(self):
        return self._shop_contact_name

    @shop_contact_name.setter
    def shop_contact_name(self, value):
        self._shop_contact_name = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def signed_alipay_id(self):
        return self._signed_alipay_id

    @signed_alipay_id.setter
    def signed_alipay_id(self, value):
        self._signed_alipay_id = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_created:
            if hasattr(self.gmt_created, 'to_alipay_dict'):
                params['gmt_created'] = self.gmt_created.to_alipay_dict()
            else:
                params['gmt_created'] = self.gmt_created
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.install_order_id:
            if hasattr(self.install_order_id, 'to_alipay_dict'):
                params['install_order_id'] = self.install_order_id.to_alipay_dict()
            else:
                params['install_order_id'] = self.install_order_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.new_device_sn:
            if hasattr(self.new_device_sn, 'to_alipay_dict'):
                params['new_device_sn'] = self.new_device_sn.to_alipay_dict()
            else:
                params['new_device_sn'] = self.new_device_sn
        if self.old_device_sn:
            if hasattr(self.old_device_sn, 'to_alipay_dict'):
                params['old_device_sn'] = self.old_device_sn.to_alipay_dict()
            else:
                params['old_device_sn'] = self.old_device_sn
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.problem_type:
            if hasattr(self.problem_type, 'to_alipay_dict'):
                params['problem_type'] = self.problem_type.to_alipay_dict()
            else:
                params['problem_type'] = self.problem_type
        if self.repair_mobile:
            if hasattr(self.repair_mobile, 'to_alipay_dict'):
                params['repair_mobile'] = self.repair_mobile.to_alipay_dict()
            else:
                params['repair_mobile'] = self.repair_mobile
        if self.repair_name:
            if hasattr(self.repair_name, 'to_alipay_dict'):
                params['repair_name'] = self.repair_name.to_alipay_dict()
            else:
                params['repair_name'] = self.repair_name
        if self.shop_contact_mobile:
            if hasattr(self.shop_contact_mobile, 'to_alipay_dict'):
                params['shop_contact_mobile'] = self.shop_contact_mobile.to_alipay_dict()
            else:
                params['shop_contact_mobile'] = self.shop_contact_mobile
        if self.shop_contact_name:
            if hasattr(self.shop_contact_name, 'to_alipay_dict'):
                params['shop_contact_name'] = self.shop_contact_name.to_alipay_dict()
            else:
                params['shop_contact_name'] = self.shop_contact_name
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.signed_alipay_id:
            if hasattr(self.signed_alipay_id, 'to_alipay_dict'):
                params['signed_alipay_id'] = self.signed_alipay_id.to_alipay_dict()
            else:
                params['signed_alipay_id'] = self.signed_alipay_id
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIotdeviceMaintenanceModifyModel()
        if 'gmt_created' in d:
            o.gmt_created = d['gmt_created']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'install_order_id' in d:
            o.install_order_id = d['install_order_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'new_device_sn' in d:
            o.new_device_sn = d['new_device_sn']
        if 'old_device_sn' in d:
            o.old_device_sn = d['old_device_sn']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'problem_type' in d:
            o.problem_type = d['problem_type']
        if 'repair_mobile' in d:
            o.repair_mobile = d['repair_mobile']
        if 'repair_name' in d:
            o.repair_name = d['repair_name']
        if 'shop_contact_mobile' in d:
            o.shop_contact_mobile = d['shop_contact_mobile']
        if 'shop_contact_name' in d:
            o.shop_contact_name = d['shop_contact_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'signed_alipay_id' in d:
            o.signed_alipay_id = d['signed_alipay_id']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        return o


