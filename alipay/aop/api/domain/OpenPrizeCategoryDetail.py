#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenPrizeCategoryDetail(object):

    def __init__(self):
        self._available_receive = None
        self._category_available_receive = None
        self._current_group_receive = None
        self._current_receive = None
        self._from_amount = None
        self._group_available_receive = None
        self._group_limit = None
        self._group_real_available_receive = None
        self._group_view_order = None
        self._inner_view_order = None
        self._prize_id = None
        self._reach_category_limit = None
        self._reach_group_limit = None
        self._reach_upper_limit = None
        self._receive_limit = None
        self._remain_budget = None
        self._status = None
        self._template_id = None
        self._to_amount = None
        self._voucher_biz_code = None

    @property
    def available_receive(self):
        return self._available_receive

    @available_receive.setter
    def available_receive(self, value):
        self._available_receive = value
    @property
    def category_available_receive(self):
        return self._category_available_receive

    @category_available_receive.setter
    def category_available_receive(self, value):
        self._category_available_receive = value
    @property
    def current_group_receive(self):
        return self._current_group_receive

    @current_group_receive.setter
    def current_group_receive(self, value):
        self._current_group_receive = value
    @property
    def current_receive(self):
        return self._current_receive

    @current_receive.setter
    def current_receive(self, value):
        self._current_receive = value
    @property
    def from_amount(self):
        return self._from_amount

    @from_amount.setter
    def from_amount(self, value):
        self._from_amount = value
    @property
    def group_available_receive(self):
        return self._group_available_receive

    @group_available_receive.setter
    def group_available_receive(self, value):
        self._group_available_receive = value
    @property
    def group_limit(self):
        return self._group_limit

    @group_limit.setter
    def group_limit(self, value):
        self._group_limit = value
    @property
    def group_real_available_receive(self):
        return self._group_real_available_receive

    @group_real_available_receive.setter
    def group_real_available_receive(self, value):
        self._group_real_available_receive = value
    @property
    def group_view_order(self):
        return self._group_view_order

    @group_view_order.setter
    def group_view_order(self, value):
        self._group_view_order = value
    @property
    def inner_view_order(self):
        return self._inner_view_order

    @inner_view_order.setter
    def inner_view_order(self, value):
        self._inner_view_order = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def reach_category_limit(self):
        return self._reach_category_limit

    @reach_category_limit.setter
    def reach_category_limit(self, value):
        self._reach_category_limit = value
    @property
    def reach_group_limit(self):
        return self._reach_group_limit

    @reach_group_limit.setter
    def reach_group_limit(self, value):
        self._reach_group_limit = value
    @property
    def reach_upper_limit(self):
        return self._reach_upper_limit

    @reach_upper_limit.setter
    def reach_upper_limit(self, value):
        self._reach_upper_limit = value
    @property
    def receive_limit(self):
        return self._receive_limit

    @receive_limit.setter
    def receive_limit(self, value):
        self._receive_limit = value
    @property
    def remain_budget(self):
        return self._remain_budget

    @remain_budget.setter
    def remain_budget(self, value):
        self._remain_budget = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def to_amount(self):
        return self._to_amount

    @to_amount.setter
    def to_amount(self, value):
        self._to_amount = value
    @property
    def voucher_biz_code(self):
        return self._voucher_biz_code

    @voucher_biz_code.setter
    def voucher_biz_code(self, value):
        self._voucher_biz_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_receive:
            if hasattr(self.available_receive, 'to_alipay_dict'):
                params['available_receive'] = self.available_receive.to_alipay_dict()
            else:
                params['available_receive'] = self.available_receive
        if self.category_available_receive:
            if hasattr(self.category_available_receive, 'to_alipay_dict'):
                params['category_available_receive'] = self.category_available_receive.to_alipay_dict()
            else:
                params['category_available_receive'] = self.category_available_receive
        if self.current_group_receive:
            if hasattr(self.current_group_receive, 'to_alipay_dict'):
                params['current_group_receive'] = self.current_group_receive.to_alipay_dict()
            else:
                params['current_group_receive'] = self.current_group_receive
        if self.current_receive:
            if hasattr(self.current_receive, 'to_alipay_dict'):
                params['current_receive'] = self.current_receive.to_alipay_dict()
            else:
                params['current_receive'] = self.current_receive
        if self.from_amount:
            if hasattr(self.from_amount, 'to_alipay_dict'):
                params['from_amount'] = self.from_amount.to_alipay_dict()
            else:
                params['from_amount'] = self.from_amount
        if self.group_available_receive:
            if hasattr(self.group_available_receive, 'to_alipay_dict'):
                params['group_available_receive'] = self.group_available_receive.to_alipay_dict()
            else:
                params['group_available_receive'] = self.group_available_receive
        if self.group_limit:
            if hasattr(self.group_limit, 'to_alipay_dict'):
                params['group_limit'] = self.group_limit.to_alipay_dict()
            else:
                params['group_limit'] = self.group_limit
        if self.group_real_available_receive:
            if hasattr(self.group_real_available_receive, 'to_alipay_dict'):
                params['group_real_available_receive'] = self.group_real_available_receive.to_alipay_dict()
            else:
                params['group_real_available_receive'] = self.group_real_available_receive
        if self.group_view_order:
            if hasattr(self.group_view_order, 'to_alipay_dict'):
                params['group_view_order'] = self.group_view_order.to_alipay_dict()
            else:
                params['group_view_order'] = self.group_view_order
        if self.inner_view_order:
            if hasattr(self.inner_view_order, 'to_alipay_dict'):
                params['inner_view_order'] = self.inner_view_order.to_alipay_dict()
            else:
                params['inner_view_order'] = self.inner_view_order
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.reach_category_limit:
            if hasattr(self.reach_category_limit, 'to_alipay_dict'):
                params['reach_category_limit'] = self.reach_category_limit.to_alipay_dict()
            else:
                params['reach_category_limit'] = self.reach_category_limit
        if self.reach_group_limit:
            if hasattr(self.reach_group_limit, 'to_alipay_dict'):
                params['reach_group_limit'] = self.reach_group_limit.to_alipay_dict()
            else:
                params['reach_group_limit'] = self.reach_group_limit
        if self.reach_upper_limit:
            if hasattr(self.reach_upper_limit, 'to_alipay_dict'):
                params['reach_upper_limit'] = self.reach_upper_limit.to_alipay_dict()
            else:
                params['reach_upper_limit'] = self.reach_upper_limit
        if self.receive_limit:
            if hasattr(self.receive_limit, 'to_alipay_dict'):
                params['receive_limit'] = self.receive_limit.to_alipay_dict()
            else:
                params['receive_limit'] = self.receive_limit
        if self.remain_budget:
            if hasattr(self.remain_budget, 'to_alipay_dict'):
                params['remain_budget'] = self.remain_budget.to_alipay_dict()
            else:
                params['remain_budget'] = self.remain_budget
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.to_amount:
            if hasattr(self.to_amount, 'to_alipay_dict'):
                params['to_amount'] = self.to_amount.to_alipay_dict()
            else:
                params['to_amount'] = self.to_amount
        if self.voucher_biz_code:
            if hasattr(self.voucher_biz_code, 'to_alipay_dict'):
                params['voucher_biz_code'] = self.voucher_biz_code.to_alipay_dict()
            else:
                params['voucher_biz_code'] = self.voucher_biz_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPrizeCategoryDetail()
        if 'available_receive' in d:
            o.available_receive = d['available_receive']
        if 'category_available_receive' in d:
            o.category_available_receive = d['category_available_receive']
        if 'current_group_receive' in d:
            o.current_group_receive = d['current_group_receive']
        if 'current_receive' in d:
            o.current_receive = d['current_receive']
        if 'from_amount' in d:
            o.from_amount = d['from_amount']
        if 'group_available_receive' in d:
            o.group_available_receive = d['group_available_receive']
        if 'group_limit' in d:
            o.group_limit = d['group_limit']
        if 'group_real_available_receive' in d:
            o.group_real_available_receive = d['group_real_available_receive']
        if 'group_view_order' in d:
            o.group_view_order = d['group_view_order']
        if 'inner_view_order' in d:
            o.inner_view_order = d['inner_view_order']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'reach_category_limit' in d:
            o.reach_category_limit = d['reach_category_limit']
        if 'reach_group_limit' in d:
            o.reach_group_limit = d['reach_group_limit']
        if 'reach_upper_limit' in d:
            o.reach_upper_limit = d['reach_upper_limit']
        if 'receive_limit' in d:
            o.receive_limit = d['receive_limit']
        if 'remain_budget' in d:
            o.remain_budget = d['remain_budget']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'to_amount' in d:
            o.to_amount = d['to_amount']
        if 'voucher_biz_code' in d:
            o.voucher_biz_code = d['voucher_biz_code']
        return o


