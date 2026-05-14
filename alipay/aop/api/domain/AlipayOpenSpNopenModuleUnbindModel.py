#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNopenModuleUnbindModel(object):

    def __init__(self):
        self._device_item_id = None
        self._device_sn = None
        self._item_id = None
        self._mcu_id = None
        self._regenerate_link = None
        self._se_uuid = None
        self._sn = None
        self._supplier_id = None
        self._template_code = None

    @property
    def device_item_id(self):
        return self._device_item_id

    @device_item_id.setter
    def device_item_id(self, value):
        self._device_item_id = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mcu_id(self):
        return self._mcu_id

    @mcu_id.setter
    def mcu_id(self, value):
        self._mcu_id = value
    @property
    def regenerate_link(self):
        return self._regenerate_link

    @regenerate_link.setter
    def regenerate_link(self, value):
        self._regenerate_link = value
    @property
    def se_uuid(self):
        return self._se_uuid

    @se_uuid.setter
    def se_uuid(self, value):
        self._se_uuid = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_item_id:
            if hasattr(self.device_item_id, 'to_alipay_dict'):
                params['device_item_id'] = self.device_item_id.to_alipay_dict()
            else:
                params['device_item_id'] = self.device_item_id
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mcu_id:
            if hasattr(self.mcu_id, 'to_alipay_dict'):
                params['mcu_id'] = self.mcu_id.to_alipay_dict()
            else:
                params['mcu_id'] = self.mcu_id
        if self.regenerate_link:
            if hasattr(self.regenerate_link, 'to_alipay_dict'):
                params['regenerate_link'] = self.regenerate_link.to_alipay_dict()
            else:
                params['regenerate_link'] = self.regenerate_link
        if self.se_uuid:
            if hasattr(self.se_uuid, 'to_alipay_dict'):
                params['se_uuid'] = self.se_uuid.to_alipay_dict()
            else:
                params['se_uuid'] = self.se_uuid
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNopenModuleUnbindModel()
        if 'device_item_id' in d:
            o.device_item_id = d['device_item_id']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mcu_id' in d:
            o.mcu_id = d['mcu_id']
        if 'regenerate_link' in d:
            o.regenerate_link = d['regenerate_link']
        if 'se_uuid' in d:
            o.se_uuid = d['se_uuid']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


