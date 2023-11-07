#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIotfmUsersimpleinfoQueryModel(object):

    def __init__(self):
        self._access_token = None
        self._device_city_code = None
        self._fm_ins_card_id = None
        self._ftoken = None
        self._open_id = None
        self._other_open_id = None
        self._other_user_id = None
        self._term_sn = None
        self._tmnl_sn = None
        self._user_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def device_city_code(self):
        return self._device_city_code

    @device_city_code.setter
    def device_city_code(self, value):
        self._device_city_code = value
    @property
    def fm_ins_card_id(self):
        return self._fm_ins_card_id

    @fm_ins_card_id.setter
    def fm_ins_card_id(self, value):
        self._fm_ins_card_id = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def other_open_id(self):
        return self._other_open_id

    @other_open_id.setter
    def other_open_id(self, value):
        self._other_open_id = value
    @property
    def other_user_id(self):
        return self._other_user_id

    @other_user_id.setter
    def other_user_id(self, value):
        self._other_user_id = value
    @property
    def term_sn(self):
        return self._term_sn

    @term_sn.setter
    def term_sn(self, value):
        self._term_sn = value
    @property
    def tmnl_sn(self):
        return self._tmnl_sn

    @tmnl_sn.setter
    def tmnl_sn(self, value):
        self._tmnl_sn = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.device_city_code:
            if hasattr(self.device_city_code, 'to_alipay_dict'):
                params['device_city_code'] = self.device_city_code.to_alipay_dict()
            else:
                params['device_city_code'] = self.device_city_code
        if self.fm_ins_card_id:
            if hasattr(self.fm_ins_card_id, 'to_alipay_dict'):
                params['fm_ins_card_id'] = self.fm_ins_card_id.to_alipay_dict()
            else:
                params['fm_ins_card_id'] = self.fm_ins_card_id
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.other_open_id:
            if hasattr(self.other_open_id, 'to_alipay_dict'):
                params['other_open_id'] = self.other_open_id.to_alipay_dict()
            else:
                params['other_open_id'] = self.other_open_id
        if self.other_user_id:
            if hasattr(self.other_user_id, 'to_alipay_dict'):
                params['other_user_id'] = self.other_user_id.to_alipay_dict()
            else:
                params['other_user_id'] = self.other_user_id
        if self.term_sn:
            if hasattr(self.term_sn, 'to_alipay_dict'):
                params['term_sn'] = self.term_sn.to_alipay_dict()
            else:
                params['term_sn'] = self.term_sn
        if self.tmnl_sn:
            if hasattr(self.tmnl_sn, 'to_alipay_dict'):
                params['tmnl_sn'] = self.tmnl_sn.to_alipay_dict()
            else:
                params['tmnl_sn'] = self.tmnl_sn
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIotfmUsersimpleinfoQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'device_city_code' in d:
            o.device_city_code = d['device_city_code']
        if 'fm_ins_card_id' in d:
            o.fm_ins_card_id = d['fm_ins_card_id']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'other_open_id' in d:
            o.other_open_id = d['other_open_id']
        if 'other_user_id' in d:
            o.other_user_id = d['other_user_id']
        if 'term_sn' in d:
            o.term_sn = d['term_sn']
        if 'tmnl_sn' in d:
            o.tmnl_sn = d['tmnl_sn']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


