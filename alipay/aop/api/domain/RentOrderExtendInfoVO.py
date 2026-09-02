#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentMerchantUploadContractVO import RentMerchantUploadContractVO


class RentOrderExtendInfoVO(object):

    def __init__(self):
        self._ec_sign_user_authorized = None
        self._merchant_upload_contracts = None
        self._promised_send_time = None
        self._recycle_order_id = None
        self._rent_dispatch_id = None
        self._scene_id = None
        self._union_rent_tag = None

    @property
    def ec_sign_user_authorized(self):
        return self._ec_sign_user_authorized

    @ec_sign_user_authorized.setter
    def ec_sign_user_authorized(self, value):
        self._ec_sign_user_authorized = value
    @property
    def merchant_upload_contracts(self):
        return self._merchant_upload_contracts

    @merchant_upload_contracts.setter
    def merchant_upload_contracts(self, value):
        if isinstance(value, list):
            self._merchant_upload_contracts = list()
            for i in value:
                if isinstance(i, RentMerchantUploadContractVO):
                    self._merchant_upload_contracts.append(i)
                else:
                    self._merchant_upload_contracts.append(RentMerchantUploadContractVO.from_alipay_dict(i))
    @property
    def promised_send_time(self):
        return self._promised_send_time

    @promised_send_time.setter
    def promised_send_time(self, value):
        self._promised_send_time = value
    @property
    def recycle_order_id(self):
        return self._recycle_order_id

    @recycle_order_id.setter
    def recycle_order_id(self, value):
        self._recycle_order_id = value
    @property
    def rent_dispatch_id(self):
        return self._rent_dispatch_id

    @rent_dispatch_id.setter
    def rent_dispatch_id(self, value):
        self._rent_dispatch_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def union_rent_tag(self):
        return self._union_rent_tag

    @union_rent_tag.setter
    def union_rent_tag(self, value):
        self._union_rent_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.ec_sign_user_authorized:
            if hasattr(self.ec_sign_user_authorized, 'to_alipay_dict'):
                params['ec_sign_user_authorized'] = self.ec_sign_user_authorized.to_alipay_dict()
            else:
                params['ec_sign_user_authorized'] = self.ec_sign_user_authorized
        if self.merchant_upload_contracts:
            if isinstance(self.merchant_upload_contracts, list):
                for i in range(0, len(self.merchant_upload_contracts)):
                    element = self.merchant_upload_contracts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_upload_contracts[i] = element.to_alipay_dict()
            if hasattr(self.merchant_upload_contracts, 'to_alipay_dict'):
                params['merchant_upload_contracts'] = self.merchant_upload_contracts.to_alipay_dict()
            else:
                params['merchant_upload_contracts'] = self.merchant_upload_contracts
        if self.promised_send_time:
            if hasattr(self.promised_send_time, 'to_alipay_dict'):
                params['promised_send_time'] = self.promised_send_time.to_alipay_dict()
            else:
                params['promised_send_time'] = self.promised_send_time
        if self.recycle_order_id:
            if hasattr(self.recycle_order_id, 'to_alipay_dict'):
                params['recycle_order_id'] = self.recycle_order_id.to_alipay_dict()
            else:
                params['recycle_order_id'] = self.recycle_order_id
        if self.rent_dispatch_id:
            if hasattr(self.rent_dispatch_id, 'to_alipay_dict'):
                params['rent_dispatch_id'] = self.rent_dispatch_id.to_alipay_dict()
            else:
                params['rent_dispatch_id'] = self.rent_dispatch_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.union_rent_tag:
            if hasattr(self.union_rent_tag, 'to_alipay_dict'):
                params['union_rent_tag'] = self.union_rent_tag.to_alipay_dict()
            else:
                params['union_rent_tag'] = self.union_rent_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderExtendInfoVO()
        if 'ec_sign_user_authorized' in d:
            o.ec_sign_user_authorized = d['ec_sign_user_authorized']
        if 'merchant_upload_contracts' in d:
            o.merchant_upload_contracts = d['merchant_upload_contracts']
        if 'promised_send_time' in d:
            o.promised_send_time = d['promised_send_time']
        if 'recycle_order_id' in d:
            o.recycle_order_id = d['recycle_order_id']
        if 'rent_dispatch_id' in d:
            o.rent_dispatch_id = d['rent_dispatch_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'union_rent_tag' in d:
            o.union_rent_tag = d['union_rent_tag']
        return o


