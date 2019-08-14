#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceApplyOrderItemModel import DeviceApplyOrderItemModel


class AlipayCommerceIotDapplyOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrderQueryResponse, self).__init__()
        self._applicant_mobile = None
        self._applicant_name = None
        self._applicant_pid = None
        self._applicant_type = None
        self._apply_amount = None
        self._asset_apply_order_id = None
        self._asset_apply_type = None
        self._creator = None
        self._device_apply_order_item_models = None
        self._ext_info = None
        self._id = None
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
    def asset_apply_order_id(self):
        return self._asset_apply_order_id

    @asset_apply_order_id.setter
    def asset_apply_order_id(self, value):
        self._asset_apply_order_id = value
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
                if isinstance(i, DeviceApplyOrderItemModel):
                    self._device_apply_order_item_models.append(i)
                else:
                    self._device_apply_order_item_models.append(DeviceApplyOrderItemModel.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrderQueryResponse, self).parse_response_content(response_content)
        if 'applicant_mobile' in response:
            self.applicant_mobile = response['applicant_mobile']
        if 'applicant_name' in response:
            self.applicant_name = response['applicant_name']
        if 'applicant_pid' in response:
            self.applicant_pid = response['applicant_pid']
        if 'applicant_type' in response:
            self.applicant_type = response['applicant_type']
        if 'apply_amount' in response:
            self.apply_amount = response['apply_amount']
        if 'asset_apply_order_id' in response:
            self.asset_apply_order_id = response['asset_apply_order_id']
        if 'asset_apply_type' in response:
            self.asset_apply_type = response['asset_apply_type']
        if 'creator' in response:
            self.creator = response['creator']
        if 'device_apply_order_item_models' in response:
            self.device_apply_order_item_models = response['device_apply_order_item_models']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'id' in response:
            self.id = response['id']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'scene_name' in response:
            self.scene_name = response['scene_name']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'source_code' in response:
            self.source_code = response['source_code']
