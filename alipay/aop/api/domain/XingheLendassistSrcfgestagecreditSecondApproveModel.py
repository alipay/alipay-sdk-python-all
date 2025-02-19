#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistSrcfgestagecreditSecondApproveModel(object):

    def __init__(self):
        self._apply_no = None
        self._gov_enter_cert_no = None
        self._gov_enter_name = None
        self._ip_id = None
        self._leader_flag = None
        self._out_bsn_no = None
        self._out_review_result = None
        self._prod_code = None
        self._user_id_card = None
        self._user_name = None
        self._user_phone = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def gov_enter_cert_no(self):
        return self._gov_enter_cert_no

    @gov_enter_cert_no.setter
    def gov_enter_cert_no(self, value):
        self._gov_enter_cert_no = value
    @property
    def gov_enter_name(self):
        return self._gov_enter_name

    @gov_enter_name.setter
    def gov_enter_name(self, value):
        self._gov_enter_name = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def leader_flag(self):
        return self._leader_flag

    @leader_flag.setter
    def leader_flag(self, value):
        self._leader_flag = value
    @property
    def out_bsn_no(self):
        return self._out_bsn_no

    @out_bsn_no.setter
    def out_bsn_no(self, value):
        self._out_bsn_no = value
    @property
    def out_review_result(self):
        return self._out_review_result

    @out_review_result.setter
    def out_review_result(self, value):
        self._out_review_result = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def user_id_card(self):
        return self._user_id_card

    @user_id_card.setter
    def user_id_card(self, value):
        self._user_id_card = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.gov_enter_cert_no:
            if hasattr(self.gov_enter_cert_no, 'to_alipay_dict'):
                params['gov_enter_cert_no'] = self.gov_enter_cert_no.to_alipay_dict()
            else:
                params['gov_enter_cert_no'] = self.gov_enter_cert_no
        if self.gov_enter_name:
            if hasattr(self.gov_enter_name, 'to_alipay_dict'):
                params['gov_enter_name'] = self.gov_enter_name.to_alipay_dict()
            else:
                params['gov_enter_name'] = self.gov_enter_name
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.leader_flag:
            if hasattr(self.leader_flag, 'to_alipay_dict'):
                params['leader_flag'] = self.leader_flag.to_alipay_dict()
            else:
                params['leader_flag'] = self.leader_flag
        if self.out_bsn_no:
            if hasattr(self.out_bsn_no, 'to_alipay_dict'):
                params['out_bsn_no'] = self.out_bsn_no.to_alipay_dict()
            else:
                params['out_bsn_no'] = self.out_bsn_no
        if self.out_review_result:
            if hasattr(self.out_review_result, 'to_alipay_dict'):
                params['out_review_result'] = self.out_review_result.to_alipay_dict()
            else:
                params['out_review_result'] = self.out_review_result
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.user_id_card:
            if hasattr(self.user_id_card, 'to_alipay_dict'):
                params['user_id_card'] = self.user_id_card.to_alipay_dict()
            else:
                params['user_id_card'] = self.user_id_card
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistSrcfgestagecreditSecondApproveModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'gov_enter_cert_no' in d:
            o.gov_enter_cert_no = d['gov_enter_cert_no']
        if 'gov_enter_name' in d:
            o.gov_enter_name = d['gov_enter_name']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'leader_flag' in d:
            o.leader_flag = d['leader_flag']
        if 'out_bsn_no' in d:
            o.out_bsn_no = d['out_bsn_no']
        if 'out_review_result' in d:
            o.out_review_result = d['out_review_result']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'user_id_card' in d:
            o.user_id_card = d['user_id_card']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


