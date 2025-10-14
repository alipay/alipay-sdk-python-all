#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementFile import AgreementFile
from alipay.aop.api.domain.Credit import Credit
from alipay.aop.api.domain.LendDrawdown import LendDrawdown
from alipay.aop.api.domain.SupplementCategoryInfo import SupplementCategoryInfo


class XingheLendassistCarfinLendapplystatusNotifyModel(object):

    def __init__(self):
        self._agreement_file_list = None
        self._apply_no = None
        self._credit_list = None
        self._drawdown_list = None
        self._lend_apply_no = None
        self._mortgage_channel = None
        self._need_change_bind_card = None
        self._need_urgent_processing = None
        self._out_apply_no = None
        self._out_lend_apply_no = None
        self._refuse_code = None
        self._refuse_msg = None
        self._status = None
        self._supplement_category_list = None
        self._supplement_reason = None
        self._support_lend_before_mortgage = None

    @property
    def agreement_file_list(self):
        return self._agreement_file_list

    @agreement_file_list.setter
    def agreement_file_list(self, value):
        if isinstance(value, list):
            self._agreement_file_list = list()
            for i in value:
                if isinstance(i, AgreementFile):
                    self._agreement_file_list.append(i)
                else:
                    self._agreement_file_list.append(AgreementFile.from_alipay_dict(i))
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def credit_list(self):
        return self._credit_list

    @credit_list.setter
    def credit_list(self, value):
        if isinstance(value, list):
            self._credit_list = list()
            for i in value:
                if isinstance(i, Credit):
                    self._credit_list.append(i)
                else:
                    self._credit_list.append(Credit.from_alipay_dict(i))
    @property
    def drawdown_list(self):
        return self._drawdown_list

    @drawdown_list.setter
    def drawdown_list(self, value):
        if isinstance(value, list):
            self._drawdown_list = list()
            for i in value:
                if isinstance(i, LendDrawdown):
                    self._drawdown_list.append(i)
                else:
                    self._drawdown_list.append(LendDrawdown.from_alipay_dict(i))
    @property
    def lend_apply_no(self):
        return self._lend_apply_no

    @lend_apply_no.setter
    def lend_apply_no(self, value):
        self._lend_apply_no = value
    @property
    def mortgage_channel(self):
        return self._mortgage_channel

    @mortgage_channel.setter
    def mortgage_channel(self, value):
        self._mortgage_channel = value
    @property
    def need_change_bind_card(self):
        return self._need_change_bind_card

    @need_change_bind_card.setter
    def need_change_bind_card(self, value):
        self._need_change_bind_card = value
    @property
    def need_urgent_processing(self):
        return self._need_urgent_processing

    @need_urgent_processing.setter
    def need_urgent_processing(self, value):
        self._need_urgent_processing = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def out_lend_apply_no(self):
        return self._out_lend_apply_no

    @out_lend_apply_no.setter
    def out_lend_apply_no(self, value):
        self._out_lend_apply_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplement_category_list(self):
        return self._supplement_category_list

    @supplement_category_list.setter
    def supplement_category_list(self, value):
        if isinstance(value, list):
            self._supplement_category_list = list()
            for i in value:
                if isinstance(i, SupplementCategoryInfo):
                    self._supplement_category_list.append(i)
                else:
                    self._supplement_category_list.append(SupplementCategoryInfo.from_alipay_dict(i))
    @property
    def supplement_reason(self):
        return self._supplement_reason

    @supplement_reason.setter
    def supplement_reason(self, value):
        self._supplement_reason = value
    @property
    def support_lend_before_mortgage(self):
        return self._support_lend_before_mortgage

    @support_lend_before_mortgage.setter
    def support_lend_before_mortgage(self, value):
        self._support_lend_before_mortgage = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_file_list:
            if isinstance(self.agreement_file_list, list):
                for i in range(0, len(self.agreement_file_list)):
                    element = self.agreement_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_file_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_file_list, 'to_alipay_dict'):
                params['agreement_file_list'] = self.agreement_file_list.to_alipay_dict()
            else:
                params['agreement_file_list'] = self.agreement_file_list
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.credit_list:
            if isinstance(self.credit_list, list):
                for i in range(0, len(self.credit_list)):
                    element = self.credit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_list, 'to_alipay_dict'):
                params['credit_list'] = self.credit_list.to_alipay_dict()
            else:
                params['credit_list'] = self.credit_list
        if self.drawdown_list:
            if isinstance(self.drawdown_list, list):
                for i in range(0, len(self.drawdown_list)):
                    element = self.drawdown_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drawdown_list[i] = element.to_alipay_dict()
            if hasattr(self.drawdown_list, 'to_alipay_dict'):
                params['drawdown_list'] = self.drawdown_list.to_alipay_dict()
            else:
                params['drawdown_list'] = self.drawdown_list
        if self.lend_apply_no:
            if hasattr(self.lend_apply_no, 'to_alipay_dict'):
                params['lend_apply_no'] = self.lend_apply_no.to_alipay_dict()
            else:
                params['lend_apply_no'] = self.lend_apply_no
        if self.mortgage_channel:
            if hasattr(self.mortgage_channel, 'to_alipay_dict'):
                params['mortgage_channel'] = self.mortgage_channel.to_alipay_dict()
            else:
                params['mortgage_channel'] = self.mortgage_channel
        if self.need_change_bind_card:
            if hasattr(self.need_change_bind_card, 'to_alipay_dict'):
                params['need_change_bind_card'] = self.need_change_bind_card.to_alipay_dict()
            else:
                params['need_change_bind_card'] = self.need_change_bind_card
        if self.need_urgent_processing:
            if hasattr(self.need_urgent_processing, 'to_alipay_dict'):
                params['need_urgent_processing'] = self.need_urgent_processing.to_alipay_dict()
            else:
                params['need_urgent_processing'] = self.need_urgent_processing
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.out_lend_apply_no:
            if hasattr(self.out_lend_apply_no, 'to_alipay_dict'):
                params['out_lend_apply_no'] = self.out_lend_apply_no.to_alipay_dict()
            else:
                params['out_lend_apply_no'] = self.out_lend_apply_no
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplement_category_list:
            if isinstance(self.supplement_category_list, list):
                for i in range(0, len(self.supplement_category_list)):
                    element = self.supplement_category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supplement_category_list[i] = element.to_alipay_dict()
            if hasattr(self.supplement_category_list, 'to_alipay_dict'):
                params['supplement_category_list'] = self.supplement_category_list.to_alipay_dict()
            else:
                params['supplement_category_list'] = self.supplement_category_list
        if self.supplement_reason:
            if hasattr(self.supplement_reason, 'to_alipay_dict'):
                params['supplement_reason'] = self.supplement_reason.to_alipay_dict()
            else:
                params['supplement_reason'] = self.supplement_reason
        if self.support_lend_before_mortgage:
            if hasattr(self.support_lend_before_mortgage, 'to_alipay_dict'):
                params['support_lend_before_mortgage'] = self.support_lend_before_mortgage.to_alipay_dict()
            else:
                params['support_lend_before_mortgage'] = self.support_lend_before_mortgage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinLendapplystatusNotifyModel()
        if 'agreement_file_list' in d:
            o.agreement_file_list = d['agreement_file_list']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'credit_list' in d:
            o.credit_list = d['credit_list']
        if 'drawdown_list' in d:
            o.drawdown_list = d['drawdown_list']
        if 'lend_apply_no' in d:
            o.lend_apply_no = d['lend_apply_no']
        if 'mortgage_channel' in d:
            o.mortgage_channel = d['mortgage_channel']
        if 'need_change_bind_card' in d:
            o.need_change_bind_card = d['need_change_bind_card']
        if 'need_urgent_processing' in d:
            o.need_urgent_processing = d['need_urgent_processing']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_lend_apply_no' in d:
            o.out_lend_apply_no = d['out_lend_apply_no']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'status' in d:
            o.status = d['status']
        if 'supplement_category_list' in d:
            o.supplement_category_list = d['supplement_category_list']
        if 'supplement_reason' in d:
            o.supplement_reason = d['supplement_reason']
        if 'support_lend_before_mortgage' in d:
            o.support_lend_before_mortgage = d['support_lend_before_mortgage']
        return o


