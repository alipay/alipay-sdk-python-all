#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniActivityGiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniActivityGiftQueryResponse, self).__init__()
        self._amount_cent = None
        self._ceiling_amount_cent = None
        self._end_time = None
        self._floor_amount_cent = None
        self._full_redirect_url = None
        self._mini_app_id = None
        self._pid = None
        self._remain_amount = None
        self._single_user_limit = None
        self._start_time = None
        self._status = None
        self._template_id = None
        self._template_name = None
        self._total_amount = None
        self._voucher_discount_percent = None
        self._voucher_jump_url = None
        self._voucher_name = None
        self._voucher_template_id = None
        self._voucher_type = None

    @property
    def amount_cent(self):
        return self._amount_cent

    @amount_cent.setter
    def amount_cent(self, value):
        self._amount_cent = value
    @property
    def ceiling_amount_cent(self):
        return self._ceiling_amount_cent

    @ceiling_amount_cent.setter
    def ceiling_amount_cent(self, value):
        self._ceiling_amount_cent = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def floor_amount_cent(self):
        return self._floor_amount_cent

    @floor_amount_cent.setter
    def floor_amount_cent(self, value):
        self._floor_amount_cent = value
    @property
    def full_redirect_url(self):
        return self._full_redirect_url

    @full_redirect_url.setter
    def full_redirect_url(self, value):
        self._full_redirect_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def single_user_limit(self):
        return self._single_user_limit

    @single_user_limit.setter
    def single_user_limit(self, value):
        self._single_user_limit = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
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
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def voucher_discount_percent(self):
        return self._voucher_discount_percent

    @voucher_discount_percent.setter
    def voucher_discount_percent(self, value):
        self._voucher_discount_percent = value
    @property
    def voucher_jump_url(self):
        return self._voucher_jump_url

    @voucher_jump_url.setter
    def voucher_jump_url(self, value):
        self._voucher_jump_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniActivityGiftQueryResponse, self).parse_response_content(response_content)
        if 'amount_cent' in response:
            self.amount_cent = response['amount_cent']
        if 'ceiling_amount_cent' in response:
            self.ceiling_amount_cent = response['ceiling_amount_cent']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'floor_amount_cent' in response:
            self.floor_amount_cent = response['floor_amount_cent']
        if 'full_redirect_url' in response:
            self.full_redirect_url = response['full_redirect_url']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'pid' in response:
            self.pid = response['pid']
        if 'remain_amount' in response:
            self.remain_amount = response['remain_amount']
        if 'single_user_limit' in response:
            self.single_user_limit = response['single_user_limit']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'template_name' in response:
            self.template_name = response['template_name']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'voucher_discount_percent' in response:
            self.voucher_discount_percent = response['voucher_discount_percent']
        if 'voucher_jump_url' in response:
            self.voucher_jump_url = response['voucher_jump_url']
        if 'voucher_name' in response:
            self.voucher_name = response['voucher_name']
        if 'voucher_template_id' in response:
            self.voucher_template_id = response['voucher_template_id']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
