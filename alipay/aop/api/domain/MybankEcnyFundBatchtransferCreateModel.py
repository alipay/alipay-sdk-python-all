#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferDetail import TransferDetail


class MybankEcnyFundBatchtransferCreateModel(object):

    def __init__(self):
        self._memo = None
        self._out_request_from = None
        self._out_request_no = None
        self._payer_name = None
        self._payer_wallet_id = None
        self._total_amount = None
        self._total_num = None
        self._transfer_detail_list = None
        self._transfer_purpose = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_request_from(self):
        return self._out_request_from

    @out_request_from.setter
    def out_request_from(self, value):
        self._out_request_from = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_wallet_id(self):
        return self._payer_wallet_id

    @payer_wallet_id.setter
    def payer_wallet_id(self, value):
        self._payer_wallet_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def transfer_detail_list(self):
        return self._transfer_detail_list

    @transfer_detail_list.setter
    def transfer_detail_list(self, value):
        if isinstance(value, list):
            self._transfer_detail_list = list()
            for i in value:
                if isinstance(i, TransferDetail):
                    self._transfer_detail_list.append(i)
                else:
                    self._transfer_detail_list.append(TransferDetail.from_alipay_dict(i))
    @property
    def transfer_purpose(self):
        return self._transfer_purpose

    @transfer_purpose.setter
    def transfer_purpose(self, value):
        self._transfer_purpose = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_request_from:
            if hasattr(self.out_request_from, 'to_alipay_dict'):
                params['out_request_from'] = self.out_request_from.to_alipay_dict()
            else:
                params['out_request_from'] = self.out_request_from
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_wallet_id:
            if hasattr(self.payer_wallet_id, 'to_alipay_dict'):
                params['payer_wallet_id'] = self.payer_wallet_id.to_alipay_dict()
            else:
                params['payer_wallet_id'] = self.payer_wallet_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        if self.transfer_detail_list:
            if isinstance(self.transfer_detail_list, list):
                for i in range(0, len(self.transfer_detail_list)):
                    element = self.transfer_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.transfer_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.transfer_detail_list, 'to_alipay_dict'):
                params['transfer_detail_list'] = self.transfer_detail_list.to_alipay_dict()
            else:
                params['transfer_detail_list'] = self.transfer_detail_list
        if self.transfer_purpose:
            if hasattr(self.transfer_purpose, 'to_alipay_dict'):
                params['transfer_purpose'] = self.transfer_purpose.to_alipay_dict()
            else:
                params['transfer_purpose'] = self.transfer_purpose
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyFundBatchtransferCreateModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_request_from' in d:
            o.out_request_from = d['out_request_from']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_wallet_id' in d:
            o.payer_wallet_id = d['payer_wallet_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_num' in d:
            o.total_num = d['total_num']
        if 'transfer_detail_list' in d:
            o.transfer_detail_list = d['transfer_detail_list']
        if 'transfer_purpose' in d:
            o.transfer_purpose = d['transfer_purpose']
        return o


