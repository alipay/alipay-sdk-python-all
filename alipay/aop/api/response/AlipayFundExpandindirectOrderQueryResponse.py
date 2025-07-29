#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundExpandindirectOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundExpandindirectOrderQueryResponse, self).__init__()
        self._biz_scene = None
        self._create_time = None
        self._order_id = None
        self._out_biz_no = None
        self._product_code = None
        self._risk_review_remark = None
        self._secondary_partner_name = None
        self._status = None
        self._task_finish_time = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def risk_review_remark(self):
        return self._risk_review_remark

    @risk_review_remark.setter
    def risk_review_remark(self, value):
        self._risk_review_remark = value
    @property
    def secondary_partner_name(self):
        return self._secondary_partner_name

    @secondary_partner_name.setter
    def secondary_partner_name(self, value):
        self._secondary_partner_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_finish_time(self):
        return self._task_finish_time

    @task_finish_time.setter
    def task_finish_time(self, value):
        self._task_finish_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundExpandindirectOrderQueryResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'risk_review_remark' in response:
            self.risk_review_remark = response['risk_review_remark']
        if 'secondary_partner_name' in response:
            self.secondary_partner_name = response['secondary_partner_name']
        if 'status' in response:
            self.status = response['status']
        if 'task_finish_time' in response:
            self.task_finish_time = response['task_finish_time']
