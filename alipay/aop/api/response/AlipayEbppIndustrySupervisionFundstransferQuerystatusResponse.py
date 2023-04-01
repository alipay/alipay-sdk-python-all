#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionFundstransferQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionFundstransferQuerystatusResponse, self).__init__()
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._operate_no = None
        self._out_trade_no = None
        self._pay_finish_time = None
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
        self._transfer_msg = None
        self._transfer_status = None

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
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_finish_time(self):
        return self._pay_finish_time

    @pay_finish_time.setter
    def pay_finish_time(self, value):
        self._pay_finish_time = value
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
    @property
    def transfer_msg(self):
        return self._transfer_msg

    @transfer_msg.setter
    def transfer_msg(self, value):
        self._transfer_msg = value
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionFundstransferQuerystatusResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'currency' in response:
            self.currency = response['currency']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_finish_time' in response:
            self.pay_finish_time = response['pay_finish_time']
        if 'payee_account_type' in response:
            self.payee_account_type = response['payee_account_type']
        if 'payee_contact_line' in response:
            self.payee_contact_line = response['payee_contact_line']
        if 'payee_participant_id' in response:
            self.payee_participant_id = response['payee_participant_id']
        if 'payee_participant_name' in response:
            self.payee_participant_name = response['payee_participant_name']
        if 'payee_participant_type' in response:
            self.payee_participant_type = response['payee_participant_type']
        if 'payer_participant_id' in response:
            self.payer_participant_id = response['payer_participant_id']
        if 'payer_participant_type' in response:
            self.payer_participant_type = response['payer_participant_type']
        if 'relate_participant_id' in response:
            self.relate_participant_id = response['relate_participant_id']
        if 'relate_participant_type' in response:
            self.relate_participant_type = response['relate_participant_type']
        if 'remark' in response:
            self.remark = response['remark']
        if 'scene' in response:
            self.scene = response['scene']
        if 'transfer_msg' in response:
            self.transfer_msg = response['transfer_msg']
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']
