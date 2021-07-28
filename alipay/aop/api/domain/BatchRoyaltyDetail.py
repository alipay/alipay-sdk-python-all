#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.domain.SubMerchant import SubMerchant


class BatchRoyaltyDetail(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._error_code = None
        self._error_desc = None
        self._status = None
        self._trans_in_account_id = None
        self._trans_in_account_id_type = None
        self._trans_in_account_type = None
        self._trans_in_entity_id = None
        self._trans_in_entity_type = None
        self._trans_in_sub_merchant = None
        self._trans_out_entity_id = None
        self._trans_out_entity_type = None
        self._trans_out_sub_merchant = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_in_account_id(self):
        return self._trans_in_account_id

    @trans_in_account_id.setter
    def trans_in_account_id(self, value):
        self._trans_in_account_id = value
    @property
    def trans_in_account_id_type(self):
        return self._trans_in_account_id_type

    @trans_in_account_id_type.setter
    def trans_in_account_id_type(self, value):
        self._trans_in_account_id_type = value
    @property
    def trans_in_account_type(self):
        return self._trans_in_account_type

    @trans_in_account_type.setter
    def trans_in_account_type(self, value):
        self._trans_in_account_type = value
    @property
    def trans_in_entity_id(self):
        return self._trans_in_entity_id

    @trans_in_entity_id.setter
    def trans_in_entity_id(self, value):
        self._trans_in_entity_id = value
    @property
    def trans_in_entity_type(self):
        return self._trans_in_entity_type

    @trans_in_entity_type.setter
    def trans_in_entity_type(self, value):
        self._trans_in_entity_type = value
    @property
    def trans_in_sub_merchant(self):
        return self._trans_in_sub_merchant

    @trans_in_sub_merchant.setter
    def trans_in_sub_merchant(self, value):
        if isinstance(value, SubMerchant):
            self._trans_in_sub_merchant = value
        else:
            self._trans_in_sub_merchant = SubMerchant.from_alipay_dict(value)
    @property
    def trans_out_entity_id(self):
        return self._trans_out_entity_id

    @trans_out_entity_id.setter
    def trans_out_entity_id(self, value):
        self._trans_out_entity_id = value
    @property
    def trans_out_entity_type(self):
        return self._trans_out_entity_type

    @trans_out_entity_type.setter
    def trans_out_entity_type(self, value):
        self._trans_out_entity_type = value
    @property
    def trans_out_sub_merchant(self):
        return self._trans_out_sub_merchant

    @trans_out_sub_merchant.setter
    def trans_out_sub_merchant(self, value):
        if isinstance(value, SubMerchant):
            self._trans_out_sub_merchant = value
        else:
            self._trans_out_sub_merchant = SubMerchant.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trans_in_account_id:
            if hasattr(self.trans_in_account_id, 'to_alipay_dict'):
                params['trans_in_account_id'] = self.trans_in_account_id.to_alipay_dict()
            else:
                params['trans_in_account_id'] = self.trans_in_account_id
        if self.trans_in_account_id_type:
            if hasattr(self.trans_in_account_id_type, 'to_alipay_dict'):
                params['trans_in_account_id_type'] = self.trans_in_account_id_type.to_alipay_dict()
            else:
                params['trans_in_account_id_type'] = self.trans_in_account_id_type
        if self.trans_in_account_type:
            if hasattr(self.trans_in_account_type, 'to_alipay_dict'):
                params['trans_in_account_type'] = self.trans_in_account_type.to_alipay_dict()
            else:
                params['trans_in_account_type'] = self.trans_in_account_type
        if self.trans_in_entity_id:
            if hasattr(self.trans_in_entity_id, 'to_alipay_dict'):
                params['trans_in_entity_id'] = self.trans_in_entity_id.to_alipay_dict()
            else:
                params['trans_in_entity_id'] = self.trans_in_entity_id
        if self.trans_in_entity_type:
            if hasattr(self.trans_in_entity_type, 'to_alipay_dict'):
                params['trans_in_entity_type'] = self.trans_in_entity_type.to_alipay_dict()
            else:
                params['trans_in_entity_type'] = self.trans_in_entity_type
        if self.trans_in_sub_merchant:
            if hasattr(self.trans_in_sub_merchant, 'to_alipay_dict'):
                params['trans_in_sub_merchant'] = self.trans_in_sub_merchant.to_alipay_dict()
            else:
                params['trans_in_sub_merchant'] = self.trans_in_sub_merchant
        if self.trans_out_entity_id:
            if hasattr(self.trans_out_entity_id, 'to_alipay_dict'):
                params['trans_out_entity_id'] = self.trans_out_entity_id.to_alipay_dict()
            else:
                params['trans_out_entity_id'] = self.trans_out_entity_id
        if self.trans_out_entity_type:
            if hasattr(self.trans_out_entity_type, 'to_alipay_dict'):
                params['trans_out_entity_type'] = self.trans_out_entity_type.to_alipay_dict()
            else:
                params['trans_out_entity_type'] = self.trans_out_entity_type
        if self.trans_out_sub_merchant:
            if hasattr(self.trans_out_sub_merchant, 'to_alipay_dict'):
                params['trans_out_sub_merchant'] = self.trans_out_sub_merchant.to_alipay_dict()
            else:
                params['trans_out_sub_merchant'] = self.trans_out_sub_merchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchRoyaltyDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'status' in d:
            o.status = d['status']
        if 'trans_in_account_id' in d:
            o.trans_in_account_id = d['trans_in_account_id']
        if 'trans_in_account_id_type' in d:
            o.trans_in_account_id_type = d['trans_in_account_id_type']
        if 'trans_in_account_type' in d:
            o.trans_in_account_type = d['trans_in_account_type']
        if 'trans_in_entity_id' in d:
            o.trans_in_entity_id = d['trans_in_entity_id']
        if 'trans_in_entity_type' in d:
            o.trans_in_entity_type = d['trans_in_entity_type']
        if 'trans_in_sub_merchant' in d:
            o.trans_in_sub_merchant = d['trans_in_sub_merchant']
        if 'trans_out_entity_id' in d:
            o.trans_out_entity_id = d['trans_out_entity_id']
        if 'trans_out_entity_type' in d:
            o.trans_out_entity_type = d['trans_out_entity_type']
        if 'trans_out_sub_merchant' in d:
            o.trans_out_sub_merchant = d['trans_out_sub_merchant']
        return o


