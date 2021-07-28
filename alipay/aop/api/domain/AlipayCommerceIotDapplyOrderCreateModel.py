#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceApplyOrderItemDto import DeviceApplyOrderItemDto


class AlipayCommerceIotDapplyOrderCreateModel(object):

    def __init__(self):
        self._applicant_mobile = None
        self._applicant_name = None
        self._applicant_pid = None
        self._applicant_type = None
        self._apply_amount = None
        self._asset_apply_type = None
        self._creator = None
        self._device_apply_order_item_models = None
        self._ext_info = None
        self._item_mall_id = None
        self._memo = None
        self._merchant_name = None
        self._merchant_pid = None
        self._scene_code = None
        self._scene_name = None
        self._shop_id = None
        self._shop_name = None
        self._source_code = None

    @property
    def applicant_mobile(self):
        return self._applicant_mobile

    @applicant_mobile.setter
    def applicant_mobile(self, value):
        self._applicant_mobile = value
    @property
    def applicant_name(self):
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, value):
        self._applicant_name = value
    @property
    def applicant_pid(self):
        return self._applicant_pid

    @applicant_pid.setter
    def applicant_pid(self, value):
        self._applicant_pid = value
    @property
    def applicant_type(self):
        return self._applicant_type

    @applicant_type.setter
    def applicant_type(self, value):
        self._applicant_type = value
    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def asset_apply_type(self):
        return self._asset_apply_type

    @asset_apply_type.setter
    def asset_apply_type(self, value):
        self._asset_apply_type = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def device_apply_order_item_models(self):
        return self._device_apply_order_item_models

    @device_apply_order_item_models.setter
    def device_apply_order_item_models(self, value):
        if isinstance(value, list):
            self._device_apply_order_item_models = list()
            for i in value:
                if isinstance(i, DeviceApplyOrderItemDto):
                    self._device_apply_order_item_models.append(i)
                else:
                    self._device_apply_order_item_models.append(DeviceApplyOrderItemDto.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_mall_id(self):
        return self._item_mall_id

    @item_mall_id.setter
    def item_mall_id(self, value):
        self._item_mall_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant_mobile:
            if hasattr(self.applicant_mobile, 'to_alipay_dict'):
                params['applicant_mobile'] = self.applicant_mobile.to_alipay_dict()
            else:
                params['applicant_mobile'] = self.applicant_mobile
        if self.applicant_name:
            if hasattr(self.applicant_name, 'to_alipay_dict'):
                params['applicant_name'] = self.applicant_name.to_alipay_dict()
            else:
                params['applicant_name'] = self.applicant_name
        if self.applicant_pid:
            if hasattr(self.applicant_pid, 'to_alipay_dict'):
                params['applicant_pid'] = self.applicant_pid.to_alipay_dict()
            else:
                params['applicant_pid'] = self.applicant_pid
        if self.applicant_type:
            if hasattr(self.applicant_type, 'to_alipay_dict'):
                params['applicant_type'] = self.applicant_type.to_alipay_dict()
            else:
                params['applicant_type'] = self.applicant_type
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.asset_apply_type:
            if hasattr(self.asset_apply_type, 'to_alipay_dict'):
                params['asset_apply_type'] = self.asset_apply_type.to_alipay_dict()
            else:
                params['asset_apply_type'] = self.asset_apply_type
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.device_apply_order_item_models:
            if isinstance(self.device_apply_order_item_models, list):
                for i in range(0, len(self.device_apply_order_item_models)):
                    element = self.device_apply_order_item_models[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_apply_order_item_models[i] = element.to_alipay_dict()
            if hasattr(self.device_apply_order_item_models, 'to_alipay_dict'):
                params['device_apply_order_item_models'] = self.device_apply_order_item_models.to_alipay_dict()
            else:
                params['device_apply_order_item_models'] = self.device_apply_order_item_models
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_mall_id:
            if hasattr(self.item_mall_id, 'to_alipay_dict'):
                params['item_mall_id'] = self.item_mall_id.to_alipay_dict()
            else:
                params['item_mall_id'] = self.item_mall_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDapplyOrderCreateModel()
        if 'applicant_mobile' in d:
            o.applicant_mobile = d['applicant_mobile']
        if 'applicant_name' in d:
            o.applicant_name = d['applicant_name']
        if 'applicant_pid' in d:
            o.applicant_pid = d['applicant_pid']
        if 'applicant_type' in d:
            o.applicant_type = d['applicant_type']
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'asset_apply_type' in d:
            o.asset_apply_type = d['asset_apply_type']
        if 'creator' in d:
            o.creator = d['creator']
        if 'device_apply_order_item_models' in d:
            o.device_apply_order_item_models = d['device_apply_order_item_models']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_mall_id' in d:
            o.item_mall_id = d['item_mall_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'source_code' in d:
            o.source_code = d['source_code']
        return o


