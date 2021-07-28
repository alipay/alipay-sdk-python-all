#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseVoucherInfo(object):

    def __init__(self):
        self._account_id = None
        self._consumption_date = None
        self._employee_id = None
        self._extension = None
        self._gmt_create = None
        self._gmt_modified = None
        self._industry = None
        self._is_off_set = None
        self._medium = None
        self._outer_source_id = None
        self._parent_type = None
        self._voucher_amount = None
        self._voucher_date = None
        self._voucher_id = None
        self._voucher_no = None
        self._voucher_state = None
        self._voucher_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def consumption_date(self):
        return self._consumption_date

    @consumption_date.setter
    def consumption_date(self, value):
        self._consumption_date = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def is_off_set(self):
        return self._is_off_set

    @is_off_set.setter
    def is_off_set(self, value):
        self._is_off_set = value
    @property
    def medium(self):
        return self._medium

    @medium.setter
    def medium(self, value):
        self._medium = value
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def parent_type(self):
        return self._parent_type

    @parent_type.setter
    def parent_type(self, value):
        self._parent_type = value
    @property
    def voucher_amount(self):
        return self._voucher_amount

    @voucher_amount.setter
    def voucher_amount(self, value):
        self._voucher_amount = value
    @property
    def voucher_date(self):
        return self._voucher_date

    @voucher_date.setter
    def voucher_date(self, value):
        self._voucher_date = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_no(self):
        return self._voucher_no

    @voucher_no.setter
    def voucher_no(self, value):
        self._voucher_no = value
    @property
    def voucher_state(self):
        return self._voucher_state

    @voucher_state.setter
    def voucher_state(self, value):
        self._voucher_state = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.consumption_date:
            if hasattr(self.consumption_date, 'to_alipay_dict'):
                params['consumption_date'] = self.consumption_date.to_alipay_dict()
            else:
                params['consumption_date'] = self.consumption_date
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.is_off_set:
            if hasattr(self.is_off_set, 'to_alipay_dict'):
                params['is_off_set'] = self.is_off_set.to_alipay_dict()
            else:
                params['is_off_set'] = self.is_off_set
        if self.medium:
            if hasattr(self.medium, 'to_alipay_dict'):
                params['medium'] = self.medium.to_alipay_dict()
            else:
                params['medium'] = self.medium
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        if self.parent_type:
            if hasattr(self.parent_type, 'to_alipay_dict'):
                params['parent_type'] = self.parent_type.to_alipay_dict()
            else:
                params['parent_type'] = self.parent_type
        if self.voucher_amount:
            if hasattr(self.voucher_amount, 'to_alipay_dict'):
                params['voucher_amount'] = self.voucher_amount.to_alipay_dict()
            else:
                params['voucher_amount'] = self.voucher_amount
        if self.voucher_date:
            if hasattr(self.voucher_date, 'to_alipay_dict'):
                params['voucher_date'] = self.voucher_date.to_alipay_dict()
            else:
                params['voucher_date'] = self.voucher_date
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_no:
            if hasattr(self.voucher_no, 'to_alipay_dict'):
                params['voucher_no'] = self.voucher_no.to_alipay_dict()
            else:
                params['voucher_no'] = self.voucher_no
        if self.voucher_state:
            if hasattr(self.voucher_state, 'to_alipay_dict'):
                params['voucher_state'] = self.voucher_state.to_alipay_dict()
            else:
                params['voucher_state'] = self.voucher_state
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseVoucherInfo()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'consumption_date' in d:
            o.consumption_date = d['consumption_date']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'extension' in d:
            o.extension = d['extension']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'industry' in d:
            o.industry = d['industry']
        if 'is_off_set' in d:
            o.is_off_set = d['is_off_set']
        if 'medium' in d:
            o.medium = d['medium']
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        if 'parent_type' in d:
            o.parent_type = d['parent_type']
        if 'voucher_amount' in d:
            o.voucher_amount = d['voucher_amount']
        if 'voucher_date' in d:
            o.voucher_date = d['voucher_date']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_no' in d:
            o.voucher_no = d['voucher_no']
        if 'voucher_state' in d:
            o.voucher_state = d['voucher_state']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


