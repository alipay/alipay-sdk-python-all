#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdviceVO(object):

    def __init__(self):
        self._client_advice_timestamp = None
        self._client_id = None
        self._client_ref = None
        self._contra_amount = None
        self._contra_ccy = None
        self._end_to_end_id = None
        self._msg_type = None
        self._partial_trade = None
        self._payment_provider = None
        self._payment_type = None
        self._profile_id = None
        self._rate_ref = None
        self._rate_request_mode = None
        self._rate_type = None
        self._reference_field1 = None
        self._reference_field2 = None
        self._reference_field3 = None
        self._related_message_id = None
        self._request_message_id = None
        self._requested_rate = None
        self._settlement_amount = None
        self._settlement_ccy = None
        self._side = None
        self._slip_point = None
        self._source_event_code = None
        self._source_product_code = None
        self._time_zone = None
        self._trade_timestamp = None
        self._transaction_amount = None
        self._transaction_ccy = None
        self._transaction_ccy_type = None
        self._transaction_type = None
        self._value_date = None

    @property
    def client_advice_timestamp(self):
        return self._client_advice_timestamp

    @client_advice_timestamp.setter
    def client_advice_timestamp(self, value):
        self._client_advice_timestamp = value
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def client_ref(self):
        return self._client_ref

    @client_ref.setter
    def client_ref(self, value):
        self._client_ref = value
    @property
    def contra_amount(self):
        return self._contra_amount

    @contra_amount.setter
    def contra_amount(self, value):
        self._contra_amount = value
    @property
    def contra_ccy(self):
        return self._contra_ccy

    @contra_ccy.setter
    def contra_ccy(self, value):
        self._contra_ccy = value
    @property
    def end_to_end_id(self):
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, value):
        self._end_to_end_id = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def partial_trade(self):
        return self._partial_trade

    @partial_trade.setter
    def partial_trade(self, value):
        self._partial_trade = value
    @property
    def payment_provider(self):
        return self._payment_provider

    @payment_provider.setter
    def payment_provider(self, value):
        self._payment_provider = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value
    @property
    def rate_ref(self):
        return self._rate_ref

    @rate_ref.setter
    def rate_ref(self, value):
        self._rate_ref = value
    @property
    def rate_request_mode(self):
        return self._rate_request_mode

    @rate_request_mode.setter
    def rate_request_mode(self, value):
        self._rate_request_mode = value
    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, value):
        self._rate_type = value
    @property
    def reference_field1(self):
        return self._reference_field1

    @reference_field1.setter
    def reference_field1(self, value):
        self._reference_field1 = value
    @property
    def reference_field2(self):
        return self._reference_field2

    @reference_field2.setter
    def reference_field2(self, value):
        self._reference_field2 = value
    @property
    def reference_field3(self):
        return self._reference_field3

    @reference_field3.setter
    def reference_field3(self, value):
        self._reference_field3 = value
    @property
    def related_message_id(self):
        return self._related_message_id

    @related_message_id.setter
    def related_message_id(self, value):
        self._related_message_id = value
    @property
    def request_message_id(self):
        return self._request_message_id

    @request_message_id.setter
    def request_message_id(self, value):
        self._request_message_id = value
    @property
    def requested_rate(self):
        return self._requested_rate

    @requested_rate.setter
    def requested_rate(self, value):
        self._requested_rate = value
    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def settlement_ccy(self):
        return self._settlement_ccy

    @settlement_ccy.setter
    def settlement_ccy(self, value):
        self._settlement_ccy = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
    @property
    def slip_point(self):
        return self._slip_point

    @slip_point.setter
    def slip_point(self, value):
        self._slip_point = value
    @property
    def source_event_code(self):
        return self._source_event_code

    @source_event_code.setter
    def source_event_code(self, value):
        self._source_event_code = value
    @property
    def source_product_code(self):
        return self._source_product_code

    @source_product_code.setter
    def source_product_code(self, value):
        self._source_product_code = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def trade_timestamp(self):
        return self._trade_timestamp

    @trade_timestamp.setter
    def trade_timestamp(self, value):
        self._trade_timestamp = value
    @property
    def transaction_amount(self):
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self._transaction_amount = value
    @property
    def transaction_ccy(self):
        return self._transaction_ccy

    @transaction_ccy.setter
    def transaction_ccy(self, value):
        self._transaction_ccy = value
    @property
    def transaction_ccy_type(self):
        return self._transaction_ccy_type

    @transaction_ccy_type.setter
    def transaction_ccy_type(self, value):
        self._transaction_ccy_type = value
    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value
    @property
    def value_date(self):
        return self._value_date

    @value_date.setter
    def value_date(self, value):
        self._value_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_advice_timestamp:
            if hasattr(self.client_advice_timestamp, 'to_alipay_dict'):
                params['client_advice_timestamp'] = self.client_advice_timestamp.to_alipay_dict()
            else:
                params['client_advice_timestamp'] = self.client_advice_timestamp
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.client_ref:
            if hasattr(self.client_ref, 'to_alipay_dict'):
                params['client_ref'] = self.client_ref.to_alipay_dict()
            else:
                params['client_ref'] = self.client_ref
        if self.contra_amount:
            if hasattr(self.contra_amount, 'to_alipay_dict'):
                params['contra_amount'] = self.contra_amount.to_alipay_dict()
            else:
                params['contra_amount'] = self.contra_amount
        if self.contra_ccy:
            if hasattr(self.contra_ccy, 'to_alipay_dict'):
                params['contra_ccy'] = self.contra_ccy.to_alipay_dict()
            else:
                params['contra_ccy'] = self.contra_ccy
        if self.end_to_end_id:
            if hasattr(self.end_to_end_id, 'to_alipay_dict'):
                params['end_to_end_id'] = self.end_to_end_id.to_alipay_dict()
            else:
                params['end_to_end_id'] = self.end_to_end_id
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.partial_trade:
            if hasattr(self.partial_trade, 'to_alipay_dict'):
                params['partial_trade'] = self.partial_trade.to_alipay_dict()
            else:
                params['partial_trade'] = self.partial_trade
        if self.payment_provider:
            if hasattr(self.payment_provider, 'to_alipay_dict'):
                params['payment_provider'] = self.payment_provider.to_alipay_dict()
            else:
                params['payment_provider'] = self.payment_provider
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        if self.rate_ref:
            if hasattr(self.rate_ref, 'to_alipay_dict'):
                params['rate_ref'] = self.rate_ref.to_alipay_dict()
            else:
                params['rate_ref'] = self.rate_ref
        if self.rate_request_mode:
            if hasattr(self.rate_request_mode, 'to_alipay_dict'):
                params['rate_request_mode'] = self.rate_request_mode.to_alipay_dict()
            else:
                params['rate_request_mode'] = self.rate_request_mode
        if self.rate_type:
            if hasattr(self.rate_type, 'to_alipay_dict'):
                params['rate_type'] = self.rate_type.to_alipay_dict()
            else:
                params['rate_type'] = self.rate_type
        if self.reference_field1:
            if hasattr(self.reference_field1, 'to_alipay_dict'):
                params['reference_field1'] = self.reference_field1.to_alipay_dict()
            else:
                params['reference_field1'] = self.reference_field1
        if self.reference_field2:
            if hasattr(self.reference_field2, 'to_alipay_dict'):
                params['reference_field2'] = self.reference_field2.to_alipay_dict()
            else:
                params['reference_field2'] = self.reference_field2
        if self.reference_field3:
            if hasattr(self.reference_field3, 'to_alipay_dict'):
                params['reference_field3'] = self.reference_field3.to_alipay_dict()
            else:
                params['reference_field3'] = self.reference_field3
        if self.related_message_id:
            if hasattr(self.related_message_id, 'to_alipay_dict'):
                params['related_message_id'] = self.related_message_id.to_alipay_dict()
            else:
                params['related_message_id'] = self.related_message_id
        if self.request_message_id:
            if hasattr(self.request_message_id, 'to_alipay_dict'):
                params['request_message_id'] = self.request_message_id.to_alipay_dict()
            else:
                params['request_message_id'] = self.request_message_id
        if self.requested_rate:
            if hasattr(self.requested_rate, 'to_alipay_dict'):
                params['requested_rate'] = self.requested_rate.to_alipay_dict()
            else:
                params['requested_rate'] = self.requested_rate
        if self.settlement_amount:
            if hasattr(self.settlement_amount, 'to_alipay_dict'):
                params['settlement_amount'] = self.settlement_amount.to_alipay_dict()
            else:
                params['settlement_amount'] = self.settlement_amount
        if self.settlement_ccy:
            if hasattr(self.settlement_ccy, 'to_alipay_dict'):
                params['settlement_ccy'] = self.settlement_ccy.to_alipay_dict()
            else:
                params['settlement_ccy'] = self.settlement_ccy
        if self.side:
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = self.side.to_alipay_dict()
            else:
                params['side'] = self.side
        if self.slip_point:
            if hasattr(self.slip_point, 'to_alipay_dict'):
                params['slip_point'] = self.slip_point.to_alipay_dict()
            else:
                params['slip_point'] = self.slip_point
        if self.source_event_code:
            if hasattr(self.source_event_code, 'to_alipay_dict'):
                params['source_event_code'] = self.source_event_code.to_alipay_dict()
            else:
                params['source_event_code'] = self.source_event_code
        if self.source_product_code:
            if hasattr(self.source_product_code, 'to_alipay_dict'):
                params['source_product_code'] = self.source_product_code.to_alipay_dict()
            else:
                params['source_product_code'] = self.source_product_code
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        if self.trade_timestamp:
            if hasattr(self.trade_timestamp, 'to_alipay_dict'):
                params['trade_timestamp'] = self.trade_timestamp.to_alipay_dict()
            else:
                params['trade_timestamp'] = self.trade_timestamp
        if self.transaction_amount:
            if hasattr(self.transaction_amount, 'to_alipay_dict'):
                params['transaction_amount'] = self.transaction_amount.to_alipay_dict()
            else:
                params['transaction_amount'] = self.transaction_amount
        if self.transaction_ccy:
            if hasattr(self.transaction_ccy, 'to_alipay_dict'):
                params['transaction_ccy'] = self.transaction_ccy.to_alipay_dict()
            else:
                params['transaction_ccy'] = self.transaction_ccy
        if self.transaction_ccy_type:
            if hasattr(self.transaction_ccy_type, 'to_alipay_dict'):
                params['transaction_ccy_type'] = self.transaction_ccy_type.to_alipay_dict()
            else:
                params['transaction_ccy_type'] = self.transaction_ccy_type
        if self.transaction_type:
            if hasattr(self.transaction_type, 'to_alipay_dict'):
                params['transaction_type'] = self.transaction_type.to_alipay_dict()
            else:
                params['transaction_type'] = self.transaction_type
        if self.value_date:
            if hasattr(self.value_date, 'to_alipay_dict'):
                params['value_date'] = self.value_date.to_alipay_dict()
            else:
                params['value_date'] = self.value_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdviceVO()
        if 'client_advice_timestamp' in d:
            o.client_advice_timestamp = d['client_advice_timestamp']
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_ref' in d:
            o.client_ref = d['client_ref']
        if 'contra_amount' in d:
            o.contra_amount = d['contra_amount']
        if 'contra_ccy' in d:
            o.contra_ccy = d['contra_ccy']
        if 'end_to_end_id' in d:
            o.end_to_end_id = d['end_to_end_id']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'partial_trade' in d:
            o.partial_trade = d['partial_trade']
        if 'payment_provider' in d:
            o.payment_provider = d['payment_provider']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        if 'rate_ref' in d:
            o.rate_ref = d['rate_ref']
        if 'rate_request_mode' in d:
            o.rate_request_mode = d['rate_request_mode']
        if 'rate_type' in d:
            o.rate_type = d['rate_type']
        if 'reference_field1' in d:
            o.reference_field1 = d['reference_field1']
        if 'reference_field2' in d:
            o.reference_field2 = d['reference_field2']
        if 'reference_field3' in d:
            o.reference_field3 = d['reference_field3']
        if 'related_message_id' in d:
            o.related_message_id = d['related_message_id']
        if 'request_message_id' in d:
            o.request_message_id = d['request_message_id']
        if 'requested_rate' in d:
            o.requested_rate = d['requested_rate']
        if 'settlement_amount' in d:
            o.settlement_amount = d['settlement_amount']
        if 'settlement_ccy' in d:
            o.settlement_ccy = d['settlement_ccy']
        if 'side' in d:
            o.side = d['side']
        if 'slip_point' in d:
            o.slip_point = d['slip_point']
        if 'source_event_code' in d:
            o.source_event_code = d['source_event_code']
        if 'source_product_code' in d:
            o.source_product_code = d['source_product_code']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'trade_timestamp' in d:
            o.trade_timestamp = d['trade_timestamp']
        if 'transaction_amount' in d:
            o.transaction_amount = d['transaction_amount']
        if 'transaction_ccy' in d:
            o.transaction_ccy = d['transaction_ccy']
        if 'transaction_ccy_type' in d:
            o.transaction_ccy_type = d['transaction_ccy_type']
        if 'transaction_type' in d:
            o.transaction_type = d['transaction_type']
        if 'value_date' in d:
            o.value_date = d['value_date']
        return o


