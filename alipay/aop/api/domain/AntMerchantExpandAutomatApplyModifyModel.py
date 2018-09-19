#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SmartAddressInfo import SmartAddressInfo
from alipay.aop.api.domain.SmartAddressInfo import SmartAddressInfo
from alipay.aop.api.domain.SmartAutomatScene import SmartAutomatScene


class AntMerchantExpandAutomatApplyModifyModel(object):

    def __init__(self):
        self._delivery_address = None
        self._machine_cooperation_type = None
        self._machine_delivery_date = None
        self._machine_name = None
        self._machine_type = None
        self._merchant_user_id = None
        self._merchant_user_type = None
        self._point_position = None
        self._scene = None
        self._terminal_id = None

    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        if isinstance(value, SmartAddressInfo):
            self._delivery_address = value
        else:
            self._delivery_address = SmartAddressInfo.from_alipay_dict(value)
    @property
    def machine_cooperation_type(self):
        return self._machine_cooperation_type

    @machine_cooperation_type.setter
    def machine_cooperation_type(self, value):
        self._machine_cooperation_type = value
    @property
    def machine_delivery_date(self):
        return self._machine_delivery_date

    @machine_delivery_date.setter
    def machine_delivery_date(self, value):
        self._machine_delivery_date = value
    @property
    def machine_name(self):
        return self._machine_name

    @machine_name.setter
    def machine_name(self, value):
        self._machine_name = value
    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        self._machine_type = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def merchant_user_type(self):
        return self._merchant_user_type

    @merchant_user_type.setter
    def merchant_user_type(self, value):
        self._merchant_user_type = value
    @property
    def point_position(self):
        return self._point_position

    @point_position.setter
    def point_position(self, value):
        if isinstance(value, SmartAddressInfo):
            self._point_position = value
        else:
            self._point_position = SmartAddressInfo.from_alipay_dict(value)
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        if isinstance(value, SmartAutomatScene):
            self._scene = value
        else:
            self._scene = SmartAutomatScene.from_alipay_dict(value)
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.machine_cooperation_type:
            if hasattr(self.machine_cooperation_type, 'to_alipay_dict'):
                params['machine_cooperation_type'] = self.machine_cooperation_type.to_alipay_dict()
            else:
                params['machine_cooperation_type'] = self.machine_cooperation_type
        if self.machine_delivery_date:
            if hasattr(self.machine_delivery_date, 'to_alipay_dict'):
                params['machine_delivery_date'] = self.machine_delivery_date.to_alipay_dict()
            else:
                params['machine_delivery_date'] = self.machine_delivery_date
        if self.machine_name:
            if hasattr(self.machine_name, 'to_alipay_dict'):
                params['machine_name'] = self.machine_name.to_alipay_dict()
            else:
                params['machine_name'] = self.machine_name
        if self.machine_type:
            if hasattr(self.machine_type, 'to_alipay_dict'):
                params['machine_type'] = self.machine_type.to_alipay_dict()
            else:
                params['machine_type'] = self.machine_type
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.merchant_user_type:
            if hasattr(self.merchant_user_type, 'to_alipay_dict'):
                params['merchant_user_type'] = self.merchant_user_type.to_alipay_dict()
            else:
                params['merchant_user_type'] = self.merchant_user_type
        if self.point_position:
            if hasattr(self.point_position, 'to_alipay_dict'):
                params['point_position'] = self.point_position.to_alipay_dict()
            else:
                params['point_position'] = self.point_position
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAutomatApplyModifyModel()
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'machine_cooperation_type' in d:
            o.machine_cooperation_type = d['machine_cooperation_type']
        if 'machine_delivery_date' in d:
            o.machine_delivery_date = d['machine_delivery_date']
        if 'machine_name' in d:
            o.machine_name = d['machine_name']
        if 'machine_type' in d:
            o.machine_type = d['machine_type']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'merchant_user_type' in d:
            o.merchant_user_type = d['merchant_user_type']
        if 'point_position' in d:
            o.point_position = d['point_position']
        if 'scene' in d:
            o.scene = d['scene']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        return o


