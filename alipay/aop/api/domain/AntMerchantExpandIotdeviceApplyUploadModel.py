#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderDevice import OrderDevice
from alipay.aop.api.domain.OrderShop import OrderShop


class AntMerchantExpandIotdeviceApplyUploadModel(object):

    def __init__(self):
        self._agent_alipay_id = None
        self._apply_amount = None
        self._apply_type = None
        self._devices = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._item_id = None
        self._mall_item_id = None
        self._mall_name = None
        self._memo = None
        self._operated_alipay_id = None
        self._order_id = None
        self._order_status = None
        self._policy_type = None
        self._receiver_address = None
        self._receiver_city = None
        self._receiver_district = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._receiver_province = None
        self._settled_alipay_id = None
        self._shop = None
        self._signed_alipay_id = None

    @property
    def agent_alipay_id(self):
        return self._agent_alipay_id

    @agent_alipay_id.setter
    def agent_alipay_id(self, value):
        self._agent_alipay_id = value
    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def devices(self):
        return self._devices

    @devices.setter
    def devices(self, value):
        if isinstance(value, list):
            self._devices = list()
            for i in value:
                if isinstance(i, OrderDevice):
                    self._devices.append(i)
                else:
                    self._devices.append(OrderDevice.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mall_item_id(self):
        return self._mall_item_id

    @mall_item_id.setter
    def mall_item_id(self, value):
        self._mall_item_id = value
    @property
    def mall_name(self):
        return self._mall_name

    @mall_name.setter
    def mall_name(self, value):
        self._mall_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operated_alipay_id(self):
        return self._operated_alipay_id

    @operated_alipay_id.setter
    def operated_alipay_id(self, value):
        self._operated_alipay_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_city(self):
        return self._receiver_city

    @receiver_city.setter
    def receiver_city(self, value):
        self._receiver_city = value
    @property
    def receiver_district(self):
        return self._receiver_district

    @receiver_district.setter
    def receiver_district(self, value):
        self._receiver_district = value
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_province(self):
        return self._receiver_province

    @receiver_province.setter
    def receiver_province(self, value):
        self._receiver_province = value
    @property
    def settled_alipay_id(self):
        return self._settled_alipay_id

    @settled_alipay_id.setter
    def settled_alipay_id(self, value):
        self._settled_alipay_id = value
    @property
    def shop(self):
        return self._shop

    @shop.setter
    def shop(self, value):
        if isinstance(value, OrderShop):
            self._shop = value
        else:
            self._shop = OrderShop.from_alipay_dict(value)
    @property
    def signed_alipay_id(self):
        return self._signed_alipay_id

    @signed_alipay_id.setter
    def signed_alipay_id(self, value):
        self._signed_alipay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_alipay_id:
            if hasattr(self.agent_alipay_id, 'to_alipay_dict'):
                params['agent_alipay_id'] = self.agent_alipay_id.to_alipay_dict()
            else:
                params['agent_alipay_id'] = self.agent_alipay_id
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.devices:
            if isinstance(self.devices, list):
                for i in range(0, len(self.devices)):
                    element = self.devices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.devices[i] = element.to_alipay_dict()
            if hasattr(self.devices, 'to_alipay_dict'):
                params['devices'] = self.devices.to_alipay_dict()
            else:
                params['devices'] = self.devices
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mall_item_id:
            if hasattr(self.mall_item_id, 'to_alipay_dict'):
                params['mall_item_id'] = self.mall_item_id.to_alipay_dict()
            else:
                params['mall_item_id'] = self.mall_item_id
        if self.mall_name:
            if hasattr(self.mall_name, 'to_alipay_dict'):
                params['mall_name'] = self.mall_name.to_alipay_dict()
            else:
                params['mall_name'] = self.mall_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operated_alipay_id:
            if hasattr(self.operated_alipay_id, 'to_alipay_dict'):
                params['operated_alipay_id'] = self.operated_alipay_id.to_alipay_dict()
            else:
                params['operated_alipay_id'] = self.operated_alipay_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_city:
            if hasattr(self.receiver_city, 'to_alipay_dict'):
                params['receiver_city'] = self.receiver_city.to_alipay_dict()
            else:
                params['receiver_city'] = self.receiver_city
        if self.receiver_district:
            if hasattr(self.receiver_district, 'to_alipay_dict'):
                params['receiver_district'] = self.receiver_district.to_alipay_dict()
            else:
                params['receiver_district'] = self.receiver_district
        if self.receiver_mobile:
            if hasattr(self.receiver_mobile, 'to_alipay_dict'):
                params['receiver_mobile'] = self.receiver_mobile.to_alipay_dict()
            else:
                params['receiver_mobile'] = self.receiver_mobile
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_province:
            if hasattr(self.receiver_province, 'to_alipay_dict'):
                params['receiver_province'] = self.receiver_province.to_alipay_dict()
            else:
                params['receiver_province'] = self.receiver_province
        if self.settled_alipay_id:
            if hasattr(self.settled_alipay_id, 'to_alipay_dict'):
                params['settled_alipay_id'] = self.settled_alipay_id.to_alipay_dict()
            else:
                params['settled_alipay_id'] = self.settled_alipay_id
        if self.shop:
            if hasattr(self.shop, 'to_alipay_dict'):
                params['shop'] = self.shop.to_alipay_dict()
            else:
                params['shop'] = self.shop
        if self.signed_alipay_id:
            if hasattr(self.signed_alipay_id, 'to_alipay_dict'):
                params['signed_alipay_id'] = self.signed_alipay_id.to_alipay_dict()
            else:
                params['signed_alipay_id'] = self.signed_alipay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIotdeviceApplyUploadModel()
        if 'agent_alipay_id' in d:
            o.agent_alipay_id = d['agent_alipay_id']
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'devices' in d:
            o.devices = d['devices']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mall_item_id' in d:
            o.mall_item_id = d['mall_item_id']
        if 'mall_name' in d:
            o.mall_name = d['mall_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operated_alipay_id' in d:
            o.operated_alipay_id = d['operated_alipay_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_city' in d:
            o.receiver_city = d['receiver_city']
        if 'receiver_district' in d:
            o.receiver_district = d['receiver_district']
        if 'receiver_mobile' in d:
            o.receiver_mobile = d['receiver_mobile']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_province' in d:
            o.receiver_province = d['receiver_province']
        if 'settled_alipay_id' in d:
            o.settled_alipay_id = d['settled_alipay_id']
        if 'shop' in d:
            o.shop = d['shop']
        if 'signed_alipay_id' in d:
            o.signed_alipay_id = d['signed_alipay_id']
        return o


