#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcApplyorderSyncModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._biz_time = None
        self._cancel_reason = None
        self._card_no = None
        self._censor_info = None
        self._delivery_code = None
        self._delivery_name = None
        self._delivery_no = None
        self._device_no = None
        self._need_refund = None
        self._order_id = None
        self._order_status = None
        self._out_biz_no = None
        self._plate_color = None
        self._plate_no = None
        self._user_id = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def censor_info(self):
        return self._censor_info

    @censor_info.setter
    def censor_info(self, value):
        self._censor_info = value
    @property
    def delivery_code(self):
        return self._delivery_code

    @delivery_code.setter
    def delivery_code(self, value):
        self._delivery_code = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def delivery_no(self):
        return self._delivery_no

    @delivery_no.setter
    def delivery_no(self, value):
        self._delivery_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def need_refund(self):
        return self._need_refund

    @need_refund.setter
    def need_refund(self, value):
        self._need_refund = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.censor_info:
            if hasattr(self.censor_info, 'to_alipay_dict'):
                params['censor_info'] = self.censor_info.to_alipay_dict()
            else:
                params['censor_info'] = self.censor_info
        if self.delivery_code:
            if hasattr(self.delivery_code, 'to_alipay_dict'):
                params['delivery_code'] = self.delivery_code.to_alipay_dict()
            else:
                params['delivery_code'] = self.delivery_code
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.delivery_no:
            if hasattr(self.delivery_no, 'to_alipay_dict'):
                params['delivery_no'] = self.delivery_no.to_alipay_dict()
            else:
                params['delivery_no'] = self.delivery_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.need_refund:
            if hasattr(self.need_refund, 'to_alipay_dict'):
                params['need_refund'] = self.need_refund.to_alipay_dict()
            else:
                params['need_refund'] = self.need_refund
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcApplyorderSyncModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'censor_info' in d:
            o.censor_info = d['censor_info']
        if 'delivery_code' in d:
            o.delivery_code = d['delivery_code']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'delivery_no' in d:
            o.delivery_no = d['delivery_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'need_refund' in d:
            o.need_refund = d['need_refund']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


