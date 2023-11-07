#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeductionPlanResponse import DeductionPlanResponse


class AlipayCommerceCardDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCardDetailQueryResponse, self).__init__()
        self._cancel_type = None
        self._card_type = None
        self._create_date = None
        self._deduction_plan_response_list = None
        self._id = None
        self._login_id = None
        self._merchant_name = None
        self._name = None
        self._open_id = None
        self._order_id = None
        self._remain_count = None
        self._spc_template_id = None
        self._status = None
        self._total_count = None
        self._user_id = None

    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def deduction_plan_response_list(self):
        return self._deduction_plan_response_list

    @deduction_plan_response_list.setter
    def deduction_plan_response_list(self, value):
        if isinstance(value, list):
            self._deduction_plan_response_list = list()
            for i in value:
                if isinstance(i, DeductionPlanResponse):
                    self._deduction_plan_response_list.append(i)
                else:
                    self._deduction_plan_response_list.append(DeductionPlanResponse.from_alipay_dict(i))
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def spc_template_id(self):
        return self._spc_template_id

    @spc_template_id.setter
    def spc_template_id(self, value):
        self._spc_template_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCardDetailQueryResponse, self).parse_response_content(response_content)
        if 'cancel_type' in response:
            self.cancel_type = response['cancel_type']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'create_date' in response:
            self.create_date = response['create_date']
        if 'deduction_plan_response_list' in response:
            self.deduction_plan_response_list = response['deduction_plan_response_list']
        if 'id' in response:
            self.id = response['id']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'name' in response:
            self.name = response['name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'remain_count' in response:
            self.remain_count = response['remain_count']
        if 'spc_template_id' in response:
            self.spc_template_id = response['spc_template_id']
        if 'status' in response:
            self.status = response['status']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'user_id' in response:
            self.user_id = response['user_id']
