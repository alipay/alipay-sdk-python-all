#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIAmortizeExtInfo import GFAOpenAPIAmortizeExtInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo
from alipay.aop.api.domain.GFAOpenAPIParticipantInfo import GFAOpenAPIParticipantInfo


class GFAOpenAPIReverseBillAcceptance(object):

    def __init__(self):
        self._amortize_ext_info = None
        self._ar_no = None
        self._bill_amount = None
        self._biz_ev_code = None
        self._biz_pd_code = None
        self._cnl_ev_code = None
        self._cnl_pd_code = None
        self._currency = None
        self._direction = None
        self._event_code = None
        self._gmt_pay = None
        self._gmt_receive = None
        self._gmt_service = None
        self._nonpayment_amount = None
        self._out_business_no = None
        self._pay_status = None
        self._payee_participant = None
        self._payer_participant = None
        self._product_code = None
        self._properties = None
        self._real_amount = None
        self._rel_out_business_no = None
        self._rel_sub_out_business_no = None
        self._service_amount = None
        self._service_type = None
        self._settle_participant = None
        self._sign_participant = None
        self._sub_out_business_no = None
        self._system_origin = None
        self._tnt_inst_id = None

    @property
    def amortize_ext_info(self):
        return self._amortize_ext_info

    @amortize_ext_info.setter
    def amortize_ext_info(self, value):
        if isinstance(value, GFAOpenAPIAmortizeExtInfo):
            self._amortize_ext_info = value
        else:
            self._amortize_ext_info = GFAOpenAPIAmortizeExtInfo.from_alipay_dict(value)
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def biz_ev_code(self):
        return self._biz_ev_code

    @biz_ev_code.setter
    def biz_ev_code(self, value):
        self._biz_ev_code = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def cnl_ev_code(self):
        return self._cnl_ev_code

    @cnl_ev_code.setter
    def cnl_ev_code(self, value):
        self._cnl_ev_code = value
    @property
    def cnl_pd_code(self):
        return self._cnl_pd_code

    @cnl_pd_code.setter
    def cnl_pd_code(self, value):
        self._cnl_pd_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def gmt_receive(self):
        return self._gmt_receive

    @gmt_receive.setter
    def gmt_receive(self, value):
        self._gmt_receive = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def nonpayment_amount(self):
        return self._nonpayment_amount

    @nonpayment_amount.setter
    def nonpayment_amount(self, value):
        self._nonpayment_amount = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def payee_participant(self):
        return self._payee_participant

    @payee_participant.setter
    def payee_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._payee_participant = value
        else:
            self._payee_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def payer_participant(self):
        return self._payer_participant

    @payer_participant.setter
    def payer_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._payer_participant = value
        else:
            self._payer_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def rel_out_business_no(self):
        return self._rel_out_business_no

    @rel_out_business_no.setter
    def rel_out_business_no(self, value):
        self._rel_out_business_no = value
    @property
    def rel_sub_out_business_no(self):
        return self._rel_sub_out_business_no

    @rel_sub_out_business_no.setter
    def rel_sub_out_business_no(self, value):
        self._rel_sub_out_business_no = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def settle_participant(self):
        return self._settle_participant

    @settle_participant.setter
    def settle_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._settle_participant = value
        else:
            self._settle_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def sign_participant(self):
        return self._sign_participant

    @sign_participant.setter
    def sign_participant(self, value):
        if isinstance(value, GFAOpenAPIParticipantInfo):
            self._sign_participant = value
        else:
            self._sign_participant = GFAOpenAPIParticipantInfo.from_alipay_dict(value)
    @property
    def sub_out_business_no(self):
        return self._sub_out_business_no

    @sub_out_business_no.setter
    def sub_out_business_no(self, value):
        self._sub_out_business_no = value
    @property
    def system_origin(self):
        return self._system_origin

    @system_origin.setter
    def system_origin(self, value):
        self._system_origin = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amortize_ext_info:
            if hasattr(self.amortize_ext_info, 'to_alipay_dict'):
                params['amortize_ext_info'] = self.amortize_ext_info.to_alipay_dict()
            else:
                params['amortize_ext_info'] = self.amortize_ext_info
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.biz_ev_code:
            if hasattr(self.biz_ev_code, 'to_alipay_dict'):
                params['biz_ev_code'] = self.biz_ev_code.to_alipay_dict()
            else:
                params['biz_ev_code'] = self.biz_ev_code
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.cnl_ev_code:
            if hasattr(self.cnl_ev_code, 'to_alipay_dict'):
                params['cnl_ev_code'] = self.cnl_ev_code.to_alipay_dict()
            else:
                params['cnl_ev_code'] = self.cnl_ev_code
        if self.cnl_pd_code:
            if hasattr(self.cnl_pd_code, 'to_alipay_dict'):
                params['cnl_pd_code'] = self.cnl_pd_code.to_alipay_dict()
            else:
                params['cnl_pd_code'] = self.cnl_pd_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.gmt_receive:
            if hasattr(self.gmt_receive, 'to_alipay_dict'):
                params['gmt_receive'] = self.gmt_receive.to_alipay_dict()
            else:
                params['gmt_receive'] = self.gmt_receive
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.nonpayment_amount:
            if hasattr(self.nonpayment_amount, 'to_alipay_dict'):
                params['nonpayment_amount'] = self.nonpayment_amount.to_alipay_dict()
            else:
                params['nonpayment_amount'] = self.nonpayment_amount
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.payee_participant:
            if hasattr(self.payee_participant, 'to_alipay_dict'):
                params['payee_participant'] = self.payee_participant.to_alipay_dict()
            else:
                params['payee_participant'] = self.payee_participant
        if self.payer_participant:
            if hasattr(self.payer_participant, 'to_alipay_dict'):
                params['payer_participant'] = self.payer_participant.to_alipay_dict()
            else:
                params['payer_participant'] = self.payer_participant
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.rel_out_business_no:
            if hasattr(self.rel_out_business_no, 'to_alipay_dict'):
                params['rel_out_business_no'] = self.rel_out_business_no.to_alipay_dict()
            else:
                params['rel_out_business_no'] = self.rel_out_business_no
        if self.rel_sub_out_business_no:
            if hasattr(self.rel_sub_out_business_no, 'to_alipay_dict'):
                params['rel_sub_out_business_no'] = self.rel_sub_out_business_no.to_alipay_dict()
            else:
                params['rel_sub_out_business_no'] = self.rel_sub_out_business_no
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.settle_participant:
            if hasattr(self.settle_participant, 'to_alipay_dict'):
                params['settle_participant'] = self.settle_participant.to_alipay_dict()
            else:
                params['settle_participant'] = self.settle_participant
        if self.sign_participant:
            if hasattr(self.sign_participant, 'to_alipay_dict'):
                params['sign_participant'] = self.sign_participant.to_alipay_dict()
            else:
                params['sign_participant'] = self.sign_participant
        if self.sub_out_business_no:
            if hasattr(self.sub_out_business_no, 'to_alipay_dict'):
                params['sub_out_business_no'] = self.sub_out_business_no.to_alipay_dict()
            else:
                params['sub_out_business_no'] = self.sub_out_business_no
        if self.system_origin:
            if hasattr(self.system_origin, 'to_alipay_dict'):
                params['system_origin'] = self.system_origin.to_alipay_dict()
            else:
                params['system_origin'] = self.system_origin
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIReverseBillAcceptance()
        if 'amortize_ext_info' in d:
            o.amortize_ext_info = d['amortize_ext_info']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'biz_ev_code' in d:
            o.biz_ev_code = d['biz_ev_code']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'cnl_ev_code' in d:
            o.cnl_ev_code = d['cnl_ev_code']
        if 'cnl_pd_code' in d:
            o.cnl_pd_code = d['cnl_pd_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'direction' in d:
            o.direction = d['direction']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'gmt_receive' in d:
            o.gmt_receive = d['gmt_receive']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'nonpayment_amount' in d:
            o.nonpayment_amount = d['nonpayment_amount']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'payee_participant' in d:
            o.payee_participant = d['payee_participant']
        if 'payer_participant' in d:
            o.payer_participant = d['payer_participant']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'properties' in d:
            o.properties = d['properties']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'rel_out_business_no' in d:
            o.rel_out_business_no = d['rel_out_business_no']
        if 'rel_sub_out_business_no' in d:
            o.rel_sub_out_business_no = d['rel_sub_out_business_no']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'settle_participant' in d:
            o.settle_participant = d['settle_participant']
        if 'sign_participant' in d:
            o.sign_participant = d['sign_participant']
        if 'sub_out_business_no' in d:
            o.sub_out_business_no = d['sub_out_business_no']
        if 'system_origin' in d:
            o.system_origin = d['system_origin']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


