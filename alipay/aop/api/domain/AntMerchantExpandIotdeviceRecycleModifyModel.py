#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIotdeviceRecycleModifyModel(object):

    def __init__(self):
        self._device_sn = None
        self._gmt_created = None
        self._gmt_modified = None
        self._install_order_id = None
        self._memo = None
        self._order_id = None
        self._recycle_mobile = None
        self._recycle_name = None
        self._recycle_reason = None
        self._report_mobile = None
        self._report_name = None
        self._shop_contact_mobile = None
        self._shop_contact_name = None
        self._signed_alipay_id = None
        self._supplier_sn = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
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
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def recycle_mobile(self):
        return self._recycle_mobile

    @recycle_mobile.setter
    def recycle_mobile(self, value):
        self._recycle_mobile = value
    @property
    def recycle_name(self):
        return self._recycle_name

    @recycle_name.setter
    def recycle_name(self, value):
        self._recycle_name = value
    @property
    def recycle_reason(self):
        return self._recycle_reason

    @recycle_reason.setter
    def recycle_reason(self, value):
        self._recycle_reason = value
    @property
    def report_mobile(self):
        return self._report_mobile

    @report_mobile.setter
    def report_mobile(self, value):
        self._report_mobile = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
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
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
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
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.recycle_mobile:
            if hasattr(self.recycle_mobile, 'to_alipay_dict'):
                params['recycle_mobile'] = self.recycle_mobile.to_alipay_dict()
            else:
                params['recycle_mobile'] = self.recycle_mobile
        if self.recycle_name:
            if hasattr(self.recycle_name, 'to_alipay_dict'):
                params['recycle_name'] = self.recycle_name.to_alipay_dict()
            else:
                params['recycle_name'] = self.recycle_name
        if self.recycle_reason:
            if hasattr(self.recycle_reason, 'to_alipay_dict'):
                params['recycle_reason'] = self.recycle_reason.to_alipay_dict()
            else:
                params['recycle_reason'] = self.recycle_reason
        if self.report_mobile:
            if hasattr(self.report_mobile, 'to_alipay_dict'):
                params['report_mobile'] = self.report_mobile.to_alipay_dict()
            else:
                params['report_mobile'] = self.report_mobile
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
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
        o = AntMerchantExpandIotdeviceRecycleModifyModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'gmt_created' in d:
            o.gmt_created = d['gmt_created']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'install_order_id' in d:
            o.install_order_id = d['install_order_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'recycle_mobile' in d:
            o.recycle_mobile = d['recycle_mobile']
        if 'recycle_name' in d:
            o.recycle_name = d['recycle_name']
        if 'recycle_reason' in d:
            o.recycle_reason = d['recycle_reason']
        if 'report_mobile' in d:
            o.report_mobile = d['report_mobile']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'shop_contact_mobile' in d:
            o.shop_contact_mobile = d['shop_contact_mobile']
        if 'shop_contact_name' in d:
            o.shop_contact_name = d['shop_contact_name']
        if 'signed_alipay_id' in d:
            o.signed_alipay_id = d['signed_alipay_id']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        return o


