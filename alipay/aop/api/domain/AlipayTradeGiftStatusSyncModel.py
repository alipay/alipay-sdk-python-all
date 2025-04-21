#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeGiftStatusSyncModel(object):

    def __init__(self):
        self._gift_status = None
        self._giver_open_id = None
        self._giver_tb_open_id = None
        self._giver_tb_user_id = None
        self._giver_user_id = None
        self._present_session_id = None
        self._recipient_open_id = None
        self._recipient_user_id = None
        self._tb_og_id = None
        self._tb_order_id = None
        self._ut_sk = None
        self._wx_js_min_version = None

    @property
    def gift_status(self):
        return self._gift_status

    @gift_status.setter
    def gift_status(self, value):
        self._gift_status = value
    @property
    def giver_open_id(self):
        return self._giver_open_id

    @giver_open_id.setter
    def giver_open_id(self, value):
        self._giver_open_id = value
    @property
    def giver_tb_open_id(self):
        return self._giver_tb_open_id

    @giver_tb_open_id.setter
    def giver_tb_open_id(self, value):
        self._giver_tb_open_id = value
    @property
    def giver_tb_user_id(self):
        return self._giver_tb_user_id

    @giver_tb_user_id.setter
    def giver_tb_user_id(self, value):
        self._giver_tb_user_id = value
    @property
    def giver_user_id(self):
        return self._giver_user_id

    @giver_user_id.setter
    def giver_user_id(self, value):
        self._giver_user_id = value
    @property
    def present_session_id(self):
        return self._present_session_id

    @present_session_id.setter
    def present_session_id(self, value):
        self._present_session_id = value
    @property
    def recipient_open_id(self):
        return self._recipient_open_id

    @recipient_open_id.setter
    def recipient_open_id(self, value):
        self._recipient_open_id = value
    @property
    def recipient_user_id(self):
        return self._recipient_user_id

    @recipient_user_id.setter
    def recipient_user_id(self, value):
        self._recipient_user_id = value
    @property
    def tb_og_id(self):
        return self._tb_og_id

    @tb_og_id.setter
    def tb_og_id(self, value):
        self._tb_og_id = value
    @property
    def tb_order_id(self):
        return self._tb_order_id

    @tb_order_id.setter
    def tb_order_id(self, value):
        self._tb_order_id = value
    @property
    def ut_sk(self):
        return self._ut_sk

    @ut_sk.setter
    def ut_sk(self, value):
        self._ut_sk = value
    @property
    def wx_js_min_version(self):
        return self._wx_js_min_version

    @wx_js_min_version.setter
    def wx_js_min_version(self, value):
        self._wx_js_min_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.gift_status:
            if hasattr(self.gift_status, 'to_alipay_dict'):
                params['gift_status'] = self.gift_status.to_alipay_dict()
            else:
                params['gift_status'] = self.gift_status
        if self.giver_open_id:
            if hasattr(self.giver_open_id, 'to_alipay_dict'):
                params['giver_open_id'] = self.giver_open_id.to_alipay_dict()
            else:
                params['giver_open_id'] = self.giver_open_id
        if self.giver_tb_open_id:
            if hasattr(self.giver_tb_open_id, 'to_alipay_dict'):
                params['giver_tb_open_id'] = self.giver_tb_open_id.to_alipay_dict()
            else:
                params['giver_tb_open_id'] = self.giver_tb_open_id
        if self.giver_tb_user_id:
            if hasattr(self.giver_tb_user_id, 'to_alipay_dict'):
                params['giver_tb_user_id'] = self.giver_tb_user_id.to_alipay_dict()
            else:
                params['giver_tb_user_id'] = self.giver_tb_user_id
        if self.giver_user_id:
            if hasattr(self.giver_user_id, 'to_alipay_dict'):
                params['giver_user_id'] = self.giver_user_id.to_alipay_dict()
            else:
                params['giver_user_id'] = self.giver_user_id
        if self.present_session_id:
            if hasattr(self.present_session_id, 'to_alipay_dict'):
                params['present_session_id'] = self.present_session_id.to_alipay_dict()
            else:
                params['present_session_id'] = self.present_session_id
        if self.recipient_open_id:
            if hasattr(self.recipient_open_id, 'to_alipay_dict'):
                params['recipient_open_id'] = self.recipient_open_id.to_alipay_dict()
            else:
                params['recipient_open_id'] = self.recipient_open_id
        if self.recipient_user_id:
            if hasattr(self.recipient_user_id, 'to_alipay_dict'):
                params['recipient_user_id'] = self.recipient_user_id.to_alipay_dict()
            else:
                params['recipient_user_id'] = self.recipient_user_id
        if self.tb_og_id:
            if hasattr(self.tb_og_id, 'to_alipay_dict'):
                params['tb_og_id'] = self.tb_og_id.to_alipay_dict()
            else:
                params['tb_og_id'] = self.tb_og_id
        if self.tb_order_id:
            if hasattr(self.tb_order_id, 'to_alipay_dict'):
                params['tb_order_id'] = self.tb_order_id.to_alipay_dict()
            else:
                params['tb_order_id'] = self.tb_order_id
        if self.ut_sk:
            if hasattr(self.ut_sk, 'to_alipay_dict'):
                params['ut_sk'] = self.ut_sk.to_alipay_dict()
            else:
                params['ut_sk'] = self.ut_sk
        if self.wx_js_min_version:
            if hasattr(self.wx_js_min_version, 'to_alipay_dict'):
                params['wx_js_min_version'] = self.wx_js_min_version.to_alipay_dict()
            else:
                params['wx_js_min_version'] = self.wx_js_min_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeGiftStatusSyncModel()
        if 'gift_status' in d:
            o.gift_status = d['gift_status']
        if 'giver_open_id' in d:
            o.giver_open_id = d['giver_open_id']
        if 'giver_tb_open_id' in d:
            o.giver_tb_open_id = d['giver_tb_open_id']
        if 'giver_tb_user_id' in d:
            o.giver_tb_user_id = d['giver_tb_user_id']
        if 'giver_user_id' in d:
            o.giver_user_id = d['giver_user_id']
        if 'present_session_id' in d:
            o.present_session_id = d['present_session_id']
        if 'recipient_open_id' in d:
            o.recipient_open_id = d['recipient_open_id']
        if 'recipient_user_id' in d:
            o.recipient_user_id = d['recipient_user_id']
        if 'tb_og_id' in d:
            o.tb_og_id = d['tb_og_id']
        if 'tb_order_id' in d:
            o.tb_order_id = d['tb_order_id']
        if 'ut_sk' in d:
            o.ut_sk = d['ut_sk']
        if 'wx_js_min_version' in d:
            o.wx_js_min_version = d['wx_js_min_version']
        return o


