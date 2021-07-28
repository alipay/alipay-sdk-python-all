#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReplyRecordResponse import ReplyRecordResponse


class AlipayMerchantServiceconsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantServiceconsultQueryResponse, self).__init__()
        self._consult_event_id = None
        self._content = None
        self._gmt_create = None
        self._gmt_finished = None
        self._gmt_modified = None
        self._images = None
        self._merchant_order_no = None
        self._phone_no = None
        self._question_type = None
        self._reply_detail_infos = None
        self._second_question_type = None
        self._status = None
        self._target_id = None
        self._target_type = None
        self._trade_no = None

    @property
    def consult_event_id(self):
        return self._consult_event_id

    @consult_event_id.setter
    def consult_event_id(self, value):
        self._consult_event_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_finished(self):
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, value):
        self._gmt_finished = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value
    @property
    def reply_detail_infos(self):
        return self._reply_detail_infos

    @reply_detail_infos.setter
    def reply_detail_infos(self, value):
        if isinstance(value, list):
            self._reply_detail_infos = list()
            for i in value:
                if isinstance(i, ReplyRecordResponse):
                    self._reply_detail_infos.append(i)
                else:
                    self._reply_detail_infos.append(ReplyRecordResponse.from_alipay_dict(i))
    @property
    def second_question_type(self):
        return self._second_question_type

    @second_question_type.setter
    def second_question_type(self, value):
        self._second_question_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantServiceconsultQueryResponse, self).parse_response_content(response_content)
        if 'consult_event_id' in response:
            self.consult_event_id = response['consult_event_id']
        if 'content' in response:
            self.content = response['content']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_finished' in response:
            self.gmt_finished = response['gmt_finished']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'images' in response:
            self.images = response['images']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
        if 'question_type' in response:
            self.question_type = response['question_type']
        if 'reply_detail_infos' in response:
            self.reply_detail_infos = response['reply_detail_infos']
        if 'second_question_type' in response:
            self.second_question_type = response['second_question_type']
        if 'status' in response:
            self.status = response['status']
        if 'target_id' in response:
            self.target_id = response['target_id']
        if 'target_type' in response:
            self.target_type = response['target_type']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
