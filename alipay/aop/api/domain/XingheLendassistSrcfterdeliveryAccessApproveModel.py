#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistSrcfterdeliveryAccessApproveModel(object):

    def __init__(self):
        self._collection_flag = None
        self._collector_id_card = None
        self._collector_name = None
        self._collector_phone = None
        self._credit_apply_no = None
        self._ip_id = None
        self._out_bsn_no = None
        self._prod_code = None
        self._receipt_con_file_id = None
        self._user_id_card = None
        self._user_name = None
        self._user_phone = None

    @property
    def collection_flag(self):
        return self._collection_flag

    @collection_flag.setter
    def collection_flag(self, value):
        self._collection_flag = value
    @property
    def collector_id_card(self):
        return self._collector_id_card

    @collector_id_card.setter
    def collector_id_card(self, value):
        self._collector_id_card = value
    @property
    def collector_name(self):
        return self._collector_name

    @collector_name.setter
    def collector_name(self, value):
        self._collector_name = value
    @property
    def collector_phone(self):
        return self._collector_phone

    @collector_phone.setter
    def collector_phone(self, value):
        self._collector_phone = value
    @property
    def credit_apply_no(self):
        return self._credit_apply_no

    @credit_apply_no.setter
    def credit_apply_no(self, value):
        self._credit_apply_no = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def out_bsn_no(self):
        return self._out_bsn_no

    @out_bsn_no.setter
    def out_bsn_no(self, value):
        self._out_bsn_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def receipt_con_file_id(self):
        return self._receipt_con_file_id

    @receipt_con_file_id.setter
    def receipt_con_file_id(self, value):
        self._receipt_con_file_id = value
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
        if self.collection_flag:
            if hasattr(self.collection_flag, 'to_alipay_dict'):
                params['collection_flag'] = self.collection_flag.to_alipay_dict()
            else:
                params['collection_flag'] = self.collection_flag
        if self.collector_id_card:
            if hasattr(self.collector_id_card, 'to_alipay_dict'):
                params['collector_id_card'] = self.collector_id_card.to_alipay_dict()
            else:
                params['collector_id_card'] = self.collector_id_card
        if self.collector_name:
            if hasattr(self.collector_name, 'to_alipay_dict'):
                params['collector_name'] = self.collector_name.to_alipay_dict()
            else:
                params['collector_name'] = self.collector_name
        if self.collector_phone:
            if hasattr(self.collector_phone, 'to_alipay_dict'):
                params['collector_phone'] = self.collector_phone.to_alipay_dict()
            else:
                params['collector_phone'] = self.collector_phone
        if self.credit_apply_no:
            if hasattr(self.credit_apply_no, 'to_alipay_dict'):
                params['credit_apply_no'] = self.credit_apply_no.to_alipay_dict()
            else:
                params['credit_apply_no'] = self.credit_apply_no
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.out_bsn_no:
            if hasattr(self.out_bsn_no, 'to_alipay_dict'):
                params['out_bsn_no'] = self.out_bsn_no.to_alipay_dict()
            else:
                params['out_bsn_no'] = self.out_bsn_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.receipt_con_file_id:
            if hasattr(self.receipt_con_file_id, 'to_alipay_dict'):
                params['receipt_con_file_id'] = self.receipt_con_file_id.to_alipay_dict()
            else:
                params['receipt_con_file_id'] = self.receipt_con_file_id
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
        o = XingheLendassistSrcfterdeliveryAccessApproveModel()
        if 'collection_flag' in d:
            o.collection_flag = d['collection_flag']
        if 'collector_id_card' in d:
            o.collector_id_card = d['collector_id_card']
        if 'collector_name' in d:
            o.collector_name = d['collector_name']
        if 'collector_phone' in d:
            o.collector_phone = d['collector_phone']
        if 'credit_apply_no' in d:
            o.credit_apply_no = d['credit_apply_no']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'out_bsn_no' in d:
            o.out_bsn_no = d['out_bsn_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'receipt_con_file_id' in d:
            o.receipt_con_file_id = d['receipt_con_file_id']
        if 'user_id_card' in d:
            o.user_id_card = d['user_id_card']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


