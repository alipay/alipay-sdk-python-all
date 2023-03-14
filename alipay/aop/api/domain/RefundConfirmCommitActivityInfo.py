#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundConfirmCommitResult import RefundConfirmCommitResult


class RefundConfirmCommitActivityInfo(object):

    def __init__(self):
        self._activity_id = None
        self._refund_confirm_commit_result_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def refund_confirm_commit_result_list(self):
        return self._refund_confirm_commit_result_list

    @refund_confirm_commit_result_list.setter
    def refund_confirm_commit_result_list(self, value):
        if isinstance(value, list):
            self._refund_confirm_commit_result_list = list()
            for i in value:
                if isinstance(i, RefundConfirmCommitResult):
                    self._refund_confirm_commit_result_list.append(i)
                else:
                    self._refund_confirm_commit_result_list.append(RefundConfirmCommitResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.refund_confirm_commit_result_list:
            if isinstance(self.refund_confirm_commit_result_list, list):
                for i in range(0, len(self.refund_confirm_commit_result_list)):
                    element = self.refund_confirm_commit_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_confirm_commit_result_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_confirm_commit_result_list, 'to_alipay_dict'):
                params['refund_confirm_commit_result_list'] = self.refund_confirm_commit_result_list.to_alipay_dict()
            else:
                params['refund_confirm_commit_result_list'] = self.refund_confirm_commit_result_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundConfirmCommitActivityInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'refund_confirm_commit_result_list' in d:
            o.refund_confirm_commit_result_list = d['refund_confirm_commit_result_list']
        return o


