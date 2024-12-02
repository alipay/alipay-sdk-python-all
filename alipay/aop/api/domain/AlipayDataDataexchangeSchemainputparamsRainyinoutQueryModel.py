#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeSchemainputparamsRainyinoutQueryModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._accout_ref_id_type_openid = None
        self._boolean_01_n_select_one = None
        self._boolean_02_n_select_one = None
        self._date_01_n_select_one = None
        self._date_02_n_select_one = None
        self._num_01_n_select_one = None
        self._num_02_n_select_one = None
        self._open_id = None
        self._price_01_n_select_one = None
        self._price_02_n_select_one = None
        self._string_01_n_select_one = None
        self._string_02_n_select_one = None
        self._tc_case = None
        self._tc_mix_uid = None
        self._tc_mix_uid_ref_openid = None
        self._tc_not_uid = None
        self._tc_openid_json = None
        self._tc_pid = None
        self._tc_smid = None
        self._user_id = None
        self._user_id_ref_openid = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def accout_ref_id_type_openid(self):
        return self._accout_ref_id_type_openid

    @accout_ref_id_type_openid.setter
    def accout_ref_id_type_openid(self, value):
        self._accout_ref_id_type_openid = value
    @property
    def boolean_01_n_select_one(self):
        return self._boolean_01_n_select_one

    @boolean_01_n_select_one.setter
    def boolean_01_n_select_one(self, value):
        self._boolean_01_n_select_one = value
    @property
    def boolean_02_n_select_one(self):
        return self._boolean_02_n_select_one

    @boolean_02_n_select_one.setter
    def boolean_02_n_select_one(self, value):
        if isinstance(value, list):
            self._boolean_02_n_select_one = list()
            for i in value:
                self._boolean_02_n_select_one.append(i)
    @property
    def date_01_n_select_one(self):
        return self._date_01_n_select_one

    @date_01_n_select_one.setter
    def date_01_n_select_one(self, value):
        self._date_01_n_select_one = value
    @property
    def date_02_n_select_one(self):
        return self._date_02_n_select_one

    @date_02_n_select_one.setter
    def date_02_n_select_one(self, value):
        if isinstance(value, list):
            self._date_02_n_select_one = list()
            for i in value:
                self._date_02_n_select_one.append(i)
    @property
    def num_01_n_select_one(self):
        return self._num_01_n_select_one

    @num_01_n_select_one.setter
    def num_01_n_select_one(self, value):
        self._num_01_n_select_one = value
    @property
    def num_02_n_select_one(self):
        return self._num_02_n_select_one

    @num_02_n_select_one.setter
    def num_02_n_select_one(self, value):
        if isinstance(value, list):
            self._num_02_n_select_one = list()
            for i in value:
                self._num_02_n_select_one.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def price_01_n_select_one(self):
        return self._price_01_n_select_one

    @price_01_n_select_one.setter
    def price_01_n_select_one(self, value):
        self._price_01_n_select_one = value
    @property
    def price_02_n_select_one(self):
        return self._price_02_n_select_one

    @price_02_n_select_one.setter
    def price_02_n_select_one(self, value):
        if isinstance(value, list):
            self._price_02_n_select_one = list()
            for i in value:
                self._price_02_n_select_one.append(i)
    @property
    def string_01_n_select_one(self):
        return self._string_01_n_select_one

    @string_01_n_select_one.setter
    def string_01_n_select_one(self, value):
        self._string_01_n_select_one = value
    @property
    def string_02_n_select_one(self):
        return self._string_02_n_select_one

    @string_02_n_select_one.setter
    def string_02_n_select_one(self, value):
        if isinstance(value, list):
            self._string_02_n_select_one = list()
            for i in value:
                self._string_02_n_select_one.append(i)
    @property
    def tc_case(self):
        return self._tc_case

    @tc_case.setter
    def tc_case(self, value):
        self._tc_case = value
    @property
    def tc_mix_uid(self):
        return self._tc_mix_uid

    @tc_mix_uid.setter
    def tc_mix_uid(self, value):
        self._tc_mix_uid = value
    @property
    def tc_mix_uid_ref_openid(self):
        return self._tc_mix_uid_ref_openid

    @tc_mix_uid_ref_openid.setter
    def tc_mix_uid_ref_openid(self, value):
        self._tc_mix_uid_ref_openid = value
    @property
    def tc_not_uid(self):
        return self._tc_not_uid

    @tc_not_uid.setter
    def tc_not_uid(self, value):
        self._tc_not_uid = value
    @property
    def tc_openid_json(self):
        return self._tc_openid_json

    @tc_openid_json.setter
    def tc_openid_json(self, value):
        self._tc_openid_json = value
    @property
    def tc_pid(self):
        return self._tc_pid

    @tc_pid.setter
    def tc_pid(self, value):
        self._tc_pid = value
    @property
    def tc_smid(self):
        return self._tc_smid

    @tc_smid.setter
    def tc_smid(self, value):
        self._tc_smid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_ref_openid(self):
        return self._user_id_ref_openid

    @user_id_ref_openid.setter
    def user_id_ref_openid(self, value):
        self._user_id_ref_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.accout_ref_id_type_openid:
            if hasattr(self.accout_ref_id_type_openid, 'to_alipay_dict'):
                params['accout_ref_id_type_openid'] = self.accout_ref_id_type_openid.to_alipay_dict()
            else:
                params['accout_ref_id_type_openid'] = self.accout_ref_id_type_openid
        if self.boolean_01_n_select_one:
            if hasattr(self.boolean_01_n_select_one, 'to_alipay_dict'):
                params['boolean_01_n_select_one'] = self.boolean_01_n_select_one.to_alipay_dict()
            else:
                params['boolean_01_n_select_one'] = self.boolean_01_n_select_one
        if self.boolean_02_n_select_one:
            if isinstance(self.boolean_02_n_select_one, list):
                for i in range(0, len(self.boolean_02_n_select_one)):
                    element = self.boolean_02_n_select_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.boolean_02_n_select_one[i] = element.to_alipay_dict()
            if hasattr(self.boolean_02_n_select_one, 'to_alipay_dict'):
                params['boolean_02_n_select_one'] = self.boolean_02_n_select_one.to_alipay_dict()
            else:
                params['boolean_02_n_select_one'] = self.boolean_02_n_select_one
        if self.date_01_n_select_one:
            if hasattr(self.date_01_n_select_one, 'to_alipay_dict'):
                params['date_01_n_select_one'] = self.date_01_n_select_one.to_alipay_dict()
            else:
                params['date_01_n_select_one'] = self.date_01_n_select_one
        if self.date_02_n_select_one:
            if isinstance(self.date_02_n_select_one, list):
                for i in range(0, len(self.date_02_n_select_one)):
                    element = self.date_02_n_select_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_02_n_select_one[i] = element.to_alipay_dict()
            if hasattr(self.date_02_n_select_one, 'to_alipay_dict'):
                params['date_02_n_select_one'] = self.date_02_n_select_one.to_alipay_dict()
            else:
                params['date_02_n_select_one'] = self.date_02_n_select_one
        if self.num_01_n_select_one:
            if hasattr(self.num_01_n_select_one, 'to_alipay_dict'):
                params['num_01_n_select_one'] = self.num_01_n_select_one.to_alipay_dict()
            else:
                params['num_01_n_select_one'] = self.num_01_n_select_one
        if self.num_02_n_select_one:
            if isinstance(self.num_02_n_select_one, list):
                for i in range(0, len(self.num_02_n_select_one)):
                    element = self.num_02_n_select_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.num_02_n_select_one[i] = element.to_alipay_dict()
            if hasattr(self.num_02_n_select_one, 'to_alipay_dict'):
                params['num_02_n_select_one'] = self.num_02_n_select_one.to_alipay_dict()
            else:
                params['num_02_n_select_one'] = self.num_02_n_select_one
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.price_01_n_select_one:
            if hasattr(self.price_01_n_select_one, 'to_alipay_dict'):
                params['price_01_n_select_one'] = self.price_01_n_select_one.to_alipay_dict()
            else:
                params['price_01_n_select_one'] = self.price_01_n_select_one
        if self.price_02_n_select_one:
            if isinstance(self.price_02_n_select_one, list):
                for i in range(0, len(self.price_02_n_select_one)):
                    element = self.price_02_n_select_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_02_n_select_one[i] = element.to_alipay_dict()
            if hasattr(self.price_02_n_select_one, 'to_alipay_dict'):
                params['price_02_n_select_one'] = self.price_02_n_select_one.to_alipay_dict()
            else:
                params['price_02_n_select_one'] = self.price_02_n_select_one
        if self.string_01_n_select_one:
            if hasattr(self.string_01_n_select_one, 'to_alipay_dict'):
                params['string_01_n_select_one'] = self.string_01_n_select_one.to_alipay_dict()
            else:
                params['string_01_n_select_one'] = self.string_01_n_select_one
        if self.string_02_n_select_one:
            if isinstance(self.string_02_n_select_one, list):
                for i in range(0, len(self.string_02_n_select_one)):
                    element = self.string_02_n_select_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_02_n_select_one[i] = element.to_alipay_dict()
            if hasattr(self.string_02_n_select_one, 'to_alipay_dict'):
                params['string_02_n_select_one'] = self.string_02_n_select_one.to_alipay_dict()
            else:
                params['string_02_n_select_one'] = self.string_02_n_select_one
        if self.tc_case:
            if hasattr(self.tc_case, 'to_alipay_dict'):
                params['tc_case'] = self.tc_case.to_alipay_dict()
            else:
                params['tc_case'] = self.tc_case
        if self.tc_mix_uid:
            if hasattr(self.tc_mix_uid, 'to_alipay_dict'):
                params['tc_mix_uid'] = self.tc_mix_uid.to_alipay_dict()
            else:
                params['tc_mix_uid'] = self.tc_mix_uid
        if self.tc_mix_uid_ref_openid:
            if hasattr(self.tc_mix_uid_ref_openid, 'to_alipay_dict'):
                params['tc_mix_uid_ref_openid'] = self.tc_mix_uid_ref_openid.to_alipay_dict()
            else:
                params['tc_mix_uid_ref_openid'] = self.tc_mix_uid_ref_openid
        if self.tc_not_uid:
            if hasattr(self.tc_not_uid, 'to_alipay_dict'):
                params['tc_not_uid'] = self.tc_not_uid.to_alipay_dict()
            else:
                params['tc_not_uid'] = self.tc_not_uid
        if self.tc_openid_json:
            if hasattr(self.tc_openid_json, 'to_alipay_dict'):
                params['tc_openid_json'] = self.tc_openid_json.to_alipay_dict()
            else:
                params['tc_openid_json'] = self.tc_openid_json
        if self.tc_pid:
            if hasattr(self.tc_pid, 'to_alipay_dict'):
                params['tc_pid'] = self.tc_pid.to_alipay_dict()
            else:
                params['tc_pid'] = self.tc_pid
        if self.tc_smid:
            if hasattr(self.tc_smid, 'to_alipay_dict'):
                params['tc_smid'] = self.tc_smid.to_alipay_dict()
            else:
                params['tc_smid'] = self.tc_smid
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_ref_openid:
            if hasattr(self.user_id_ref_openid, 'to_alipay_dict'):
                params['user_id_ref_openid'] = self.user_id_ref_openid.to_alipay_dict()
            else:
                params['user_id_ref_openid'] = self.user_id_ref_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSchemainputparamsRainyinoutQueryModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'accout_ref_id_type_openid' in d:
            o.accout_ref_id_type_openid = d['accout_ref_id_type_openid']
        if 'boolean_01_n_select_one' in d:
            o.boolean_01_n_select_one = d['boolean_01_n_select_one']
        if 'boolean_02_n_select_one' in d:
            o.boolean_02_n_select_one = d['boolean_02_n_select_one']
        if 'date_01_n_select_one' in d:
            o.date_01_n_select_one = d['date_01_n_select_one']
        if 'date_02_n_select_one' in d:
            o.date_02_n_select_one = d['date_02_n_select_one']
        if 'num_01_n_select_one' in d:
            o.num_01_n_select_one = d['num_01_n_select_one']
        if 'num_02_n_select_one' in d:
            o.num_02_n_select_one = d['num_02_n_select_one']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price_01_n_select_one' in d:
            o.price_01_n_select_one = d['price_01_n_select_one']
        if 'price_02_n_select_one' in d:
            o.price_02_n_select_one = d['price_02_n_select_one']
        if 'string_01_n_select_one' in d:
            o.string_01_n_select_one = d['string_01_n_select_one']
        if 'string_02_n_select_one' in d:
            o.string_02_n_select_one = d['string_02_n_select_one']
        if 'tc_case' in d:
            o.tc_case = d['tc_case']
        if 'tc_mix_uid' in d:
            o.tc_mix_uid = d['tc_mix_uid']
        if 'tc_mix_uid_ref_openid' in d:
            o.tc_mix_uid_ref_openid = d['tc_mix_uid_ref_openid']
        if 'tc_not_uid' in d:
            o.tc_not_uid = d['tc_not_uid']
        if 'tc_openid_json' in d:
            o.tc_openid_json = d['tc_openid_json']
        if 'tc_pid' in d:
            o.tc_pid = d['tc_pid']
        if 'tc_smid' in d:
            o.tc_smid = d['tc_smid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_ref_openid' in d:
            o.user_id_ref_openid = d['user_id_ref_openid']
        return o


