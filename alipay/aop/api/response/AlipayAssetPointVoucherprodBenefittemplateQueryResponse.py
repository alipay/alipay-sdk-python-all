#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointVoucherprodBenefittemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodBenefittemplateQueryResponse, self).__init__()
        self._asset_amount = None
        self._asset_id = None
        self._asset_total_amount = None
        self._asset_type = None
        self._expire_amount = None
        self._expire_date = None
        self._publish_amount = None
        self._recycle_amount = None
        self._recycle_dt = None
        self._refund_amount = None
        self._status = None
        self._use_amount = None
        self._user_id = None

    @property
    def asset_amount(self):
        return self._asset_amount

    @asset_amount.setter
    def asset_amount(self, value):
        self._asset_amount = value
    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_total_amount(self):
        return self._asset_total_amount

    @asset_total_amount.setter
    def asset_total_amount(self, value):
        self._asset_total_amount = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def expire_amount(self):
        return self._expire_amount

    @expire_amount.setter
    def expire_amount(self, value):
        self._expire_amount = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def publish_amount(self):
        return self._publish_amount

    @publish_amount.setter
    def publish_amount(self, value):
        self._publish_amount = value
    @property
    def recycle_amount(self):
        return self._recycle_amount

    @recycle_amount.setter
    def recycle_amount(self, value):
        self._recycle_amount = value
    @property
    def recycle_dt(self):
        return self._recycle_dt

    @recycle_dt.setter
    def recycle_dt(self, value):
        self._recycle_dt = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodBenefittemplateQueryResponse, self).parse_response_content(response_content)
        if 'asset_amount' in response:
            self.asset_amount = response['asset_amount']
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'asset_total_amount' in response:
            self.asset_total_amount = response['asset_total_amount']
        if 'asset_type' in response:
            self.asset_type = response['asset_type']
        if 'expire_amount' in response:
            self.expire_amount = response['expire_amount']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'publish_amount' in response:
            self.publish_amount = response['publish_amount']
        if 'recycle_amount' in response:
            self.recycle_amount = response['recycle_amount']
        if 'recycle_dt' in response:
            self.recycle_dt = response['recycle_dt']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'status' in response:
            self.status = response['status']
        if 'use_amount' in response:
            self.use_amount = response['use_amount']
        if 'user_id' in response:
            self.user_id = response['user_id']
