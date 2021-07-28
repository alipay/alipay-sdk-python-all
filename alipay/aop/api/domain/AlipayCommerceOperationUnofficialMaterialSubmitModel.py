#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationUnofficialMaterialSubmitModel(object):

    def __init__(self):
        self._isv_pid = None
        self._mini_app_id = None
        self._qr_code_url = None
        self._rebate_pid = None
        self._seller_checkout_pid = None
        self._seller_checkout_smid = None
        self._shop_id = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def rebate_pid(self):
        return self._rebate_pid

    @rebate_pid.setter
    def rebate_pid(self, value):
        self._rebate_pid = value
    @property
    def seller_checkout_pid(self):
        return self._seller_checkout_pid

    @seller_checkout_pid.setter
    def seller_checkout_pid(self, value):
        self._seller_checkout_pid = value
    @property
    def seller_checkout_smid(self):
        return self._seller_checkout_smid

    @seller_checkout_smid.setter
    def seller_checkout_smid(self, value):
        self._seller_checkout_smid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        if self.rebate_pid:
            if hasattr(self.rebate_pid, 'to_alipay_dict'):
                params['rebate_pid'] = self.rebate_pid.to_alipay_dict()
            else:
                params['rebate_pid'] = self.rebate_pid
        if self.seller_checkout_pid:
            if hasattr(self.seller_checkout_pid, 'to_alipay_dict'):
                params['seller_checkout_pid'] = self.seller_checkout_pid.to_alipay_dict()
            else:
                params['seller_checkout_pid'] = self.seller_checkout_pid
        if self.seller_checkout_smid:
            if hasattr(self.seller_checkout_smid, 'to_alipay_dict'):
                params['seller_checkout_smid'] = self.seller_checkout_smid.to_alipay_dict()
            else:
                params['seller_checkout_smid'] = self.seller_checkout_smid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationUnofficialMaterialSubmitModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        if 'rebate_pid' in d:
            o.rebate_pid = d['rebate_pid']
        if 'seller_checkout_pid' in d:
            o.seller_checkout_pid = d['seller_checkout_pid']
        if 'seller_checkout_smid' in d:
            o.seller_checkout_smid = d['seller_checkout_smid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


