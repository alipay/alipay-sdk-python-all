#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceBindModel(object):

    def __init__(self):
        self._app_type = None
        self._application_id = None
        self._biz_tid = None
        self._device_id_type = None
        self._device_sn = None
        self._equipment_type = None
        self._external_id = None
        self._external_id_secret = None
        self._external_shop_id = None
        self._merchant_id = None
        self._merchant_id_type = None
        self._mini_app_id = None
        self._pid = None
        self._shop_id = None
        self._source = None
        self._spi_app_id = None
        self._supplier_id = None
        self._terminal_bind_info = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def device_id_type(self):
        return self._device_id_type

    @device_id_type.setter
    def device_id_type(self, value):
        self._device_id_type = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def equipment_type(self):
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, value):
        self._equipment_type = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def external_id_secret(self):
        return self._external_id_secret

    @external_id_secret.setter
    def external_id_secret(self, value):
        self._external_id_secret = value
    @property
    def external_shop_id(self):
        return self._external_shop_id

    @external_shop_id.setter
    def external_shop_id(self, value):
        self._external_shop_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_id_type(self):
        return self._merchant_id_type

    @merchant_id_type.setter
    def merchant_id_type(self, value):
        self._merchant_id_type = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def spi_app_id(self):
        return self._spi_app_id

    @spi_app_id.setter
    def spi_app_id(self, value):
        self._spi_app_id = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def terminal_bind_info(self):
        return self._terminal_bind_info

    @terminal_bind_info.setter
    def terminal_bind_info(self, value):
        self._terminal_bind_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.device_id_type:
            if hasattr(self.device_id_type, 'to_alipay_dict'):
                params['device_id_type'] = self.device_id_type.to_alipay_dict()
            else:
                params['device_id_type'] = self.device_id_type
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.equipment_type:
            if hasattr(self.equipment_type, 'to_alipay_dict'):
                params['equipment_type'] = self.equipment_type.to_alipay_dict()
            else:
                params['equipment_type'] = self.equipment_type
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.external_id_secret:
            if hasattr(self.external_id_secret, 'to_alipay_dict'):
                params['external_id_secret'] = self.external_id_secret.to_alipay_dict()
            else:
                params['external_id_secret'] = self.external_id_secret
        if self.external_shop_id:
            if hasattr(self.external_shop_id, 'to_alipay_dict'):
                params['external_shop_id'] = self.external_shop_id.to_alipay_dict()
            else:
                params['external_shop_id'] = self.external_shop_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_id_type:
            if hasattr(self.merchant_id_type, 'to_alipay_dict'):
                params['merchant_id_type'] = self.merchant_id_type.to_alipay_dict()
            else:
                params['merchant_id_type'] = self.merchant_id_type
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.spi_app_id:
            if hasattr(self.spi_app_id, 'to_alipay_dict'):
                params['spi_app_id'] = self.spi_app_id.to_alipay_dict()
            else:
                params['spi_app_id'] = self.spi_app_id
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.terminal_bind_info:
            if hasattr(self.terminal_bind_info, 'to_alipay_dict'):
                params['terminal_bind_info'] = self.terminal_bind_info.to_alipay_dict()
            else:
                params['terminal_bind_info'] = self.terminal_bind_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceBindModel()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'device_id_type' in d:
            o.device_id_type = d['device_id_type']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'equipment_type' in d:
            o.equipment_type = d['equipment_type']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'external_id_secret' in d:
            o.external_id_secret = d['external_id_secret']
        if 'external_shop_id' in d:
            o.external_shop_id = d['external_shop_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_id_type' in d:
            o.merchant_id_type = d['merchant_id_type']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source' in d:
            o.source = d['source']
        if 'spi_app_id' in d:
            o.spi_app_id = d['spi_app_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'terminal_bind_info' in d:
            o.terminal_bind_info = d['terminal_bind_info']
        return o


