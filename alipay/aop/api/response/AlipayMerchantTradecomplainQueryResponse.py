#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReplyRecordResponse import ReplyRecordResponse


class AlipayMerchantTradecomplainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantTradecomplainQueryResponse, self).__init__()
        self._complain_event_id = None
        self._complain_reason = None
        self._content = None
        self._gmt_create = None
        self._gmt_finished = None
        self._gmt_modified = None
        self._images = None
        self._leaf_category_name = None
        self._merchant_order_no = None
        self._phone_no = None
        self._reply_detail_infos = None
        self._status = None
        self._target_id = None
        self._target_type = None
        self._trade_amount = None
        self._trade_no = None

    @property
    def complain_event_id(self):
        return self._complain_event_id

    @complain_event_id.setter
    def complain_event_id(self, value):
        self._complain_event_id = value
    @property
    def complain_reason(self):
        return self._complain_reason

    @complain_reason.setter
    def complain_reason(self, value):
        self._complain_reason = value
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
    def leaf_category_name(self):
        return self._leaf_category_name

    @leaf_category_name.setter
    def leaf_category_name(self, value):
        self._leaf_category_name = value
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
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantTradecomplainQueryResponse, self).parse_response_content(response_content)
        if 'complain_event_id' in response:
            self.complain_event_id = response['complain_event_id']
        if 'complain_reason' in response:
            self.complain_reason = response['complain_reason']
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
        if 'leaf_category_name' in response:
            self.leaf_category_name = response['leaf_category_name']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
        if 'reply_detail_infos' in response:
            self.reply_detail_infos = response['reply_detail_infos']
        if 'status' in response:
            self.status = response['status']
        if 'target_id' in response:
            self.target_id = response['target_id']
        if 'target_type' in response:
            self.target_type = response['target_type']
        if 'trade_amount' in response:
            self.trade_amount = response['trade_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
