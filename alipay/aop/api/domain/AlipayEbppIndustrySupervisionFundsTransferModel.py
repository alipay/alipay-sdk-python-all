#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionFundsTransferModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._out_trade_no = None
        self._payee_account_type = None
        self._payee_contact_line = None
        self._payee_participant_id = None
        self._payee_participant_name = None
        self._payee_participant_type = None
        self._payer_participant_id = None
        self._payer_participant_type = None
        self._relate_participant_id = None
        self._relate_participant_type = None
        self._remark = None
        self._scene = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_contact_line(self):
        return self._payee_contact_line

    @payee_contact_line.setter
    def payee_contact_line(self, value):
        self._payee_contact_line = value
    @property
    def payee_participant_id(self):
        return self._payee_participant_id

    @payee_participant_id.setter
    def payee_participant_id(self, value):
        self._payee_participant_id = value
    @property
    def payee_participant_name(self):
        return self._payee_participant_name

    @payee_participant_name.setter
    def payee_participant_name(self, value):
        self._payee_participant_name = value
    @property
    def payee_participant_type(self):
        return self._payee_participant_type

    @payee_participant_type.setter
    def payee_participant_type(self, value):
        self._payee_participant_type = value
    @property
    def payer_participant_id(self):
        return self._payer_participant_id

    @payer_participant_id.setter
    def payer_participant_id(self, value):
        self._payer_participant_id = value
    @property
    def payer_participant_type(self):
        return self._payer_participant_type

    @payer_participant_type.setter
    def payer_participant_type(self, value):
        self._payer_participant_type = value
    @property
    def relate_participant_id(self):
        return self._relate_participant_id

    @relate_participant_id.setter
    def relate_participant_id(self, value):
        self._relate_participant_id = value
    @property
    def relate_participant_type(self):
        return self._relate_participant_type

    @relate_participant_type.setter
    def relate_participant_type(self, value):
        self._relate_participant_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_contact_line:
            if hasattr(self.payee_contact_line, 'to_alipay_dict'):
                params['payee_contact_line'] = self.payee_contact_line.to_alipay_dict()
            else:
                params['payee_contact_line'] = self.payee_contact_line
        if self.payee_participant_id:
            if hasattr(self.payee_participant_id, 'to_alipay_dict'):
                params['payee_participant_id'] = self.payee_participant_id.to_alipay_dict()
            else:
                params['payee_participant_id'] = self.payee_participant_id
        if self.payee_participant_name:
            if hasattr(self.payee_participant_name, 'to_alipay_dict'):
                params['payee_participant_name'] = self.payee_participant_name.to_alipay_dict()
            else:
                params['payee_participant_name'] = self.payee_participant_name
        if self.payee_participant_type:
            if hasattr(self.payee_participant_type, 'to_alipay_dict'):
                params['payee_participant_type'] = self.payee_participant_type.to_alipay_dict()
            else:
                params['payee_participant_type'] = self.payee_participant_type
        if self.payer_participant_id:
            if hasattr(self.payer_participant_id, 'to_alipay_dict'):
                params['payer_participant_id'] = self.payer_participant_id.to_alipay_dict()
            else:
                params['payer_participant_id'] = self.payer_participant_id
        if self.payer_participant_type:
            if hasattr(self.payer_participant_type, 'to_alipay_dict'):
                params['payer_participant_type'] = self.payer_participant_type.to_alipay_dict()
            else:
                params['payer_participant_type'] = self.payer_participant_type
        if self.relate_participant_id:
            if hasattr(self.relate_participant_id, 'to_alipay_dict'):
                params['relate_participant_id'] = self.relate_participant_id.to_alipay_dict()
            else:
                params['relate_participant_id'] = self.relate_participant_id
        if self.relate_participant_type:
            if hasattr(self.relate_participant_type, 'to_alipay_dict'):
                params['relate_participant_type'] = self.relate_participant_type.to_alipay_dict()
            else:
                params['relate_participant_type'] = self.relate_participant_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionFundsTransferModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'currency' in d:
            o.currency = d['currency']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_contact_line' in d:
            o.payee_contact_line = d['payee_contact_line']
        if 'payee_participant_id' in d:
            o.payee_participant_id = d['payee_participant_id']
        if 'payee_participant_name' in d:
            o.payee_participant_name = d['payee_participant_name']
        if 'payee_participant_type' in d:
            o.payee_participant_type = d['payee_participant_type']
        if 'payer_participant_id' in d:
            o.payer_participant_id = d['payer_participant_id']
        if 'payer_participant_type' in d:
            o.payer_participant_type = d['payer_participant_type']
        if 'relate_participant_id' in d:
            o.relate_participant_id = d['relate_participant_id']
        if 'relate_participant_type' in d:
            o.relate_participant_type = d['relate_participant_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene' in d:
            o.scene = d['scene']
        return o


