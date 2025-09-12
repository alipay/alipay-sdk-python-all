#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HonorCouponSendResultDTO import HonorCouponSendResultDTO
from alipay.aop.api.domain.HonorCreditApplyResultDTO import HonorCreditApplyResultDTO
from alipay.aop.api.domain.HonorLendApplyResultDTO import HonorLendApplyResultDTO
from alipay.aop.api.domain.HonorLogoffResultDTO import HonorLogoffResultDTO
from alipay.aop.api.domain.HonorRepayApplyResultDTO import HonorRepayApplyResultDTO
from alipay.aop.api.domain.HonorUnifygwCommonResult import HonorUnifygwCommonResult


class AlipayPcreditLoanHonorOpenapitestQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._coupon_send_result = None
        self._credit_apply_no = None
        self._credit_apply_result = None
        self._lend_result = None
        self._logoff_result = None
        self._open_id = None
        self._repay_result = None
        self._unifygw_result = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def coupon_send_result(self):
        return self._coupon_send_result

    @coupon_send_result.setter
    def coupon_send_result(self, value):
        if isinstance(value, HonorCouponSendResultDTO):
            self._coupon_send_result = value
        else:
            self._coupon_send_result = HonorCouponSendResultDTO.from_alipay_dict(value)
    @property
    def credit_apply_no(self):
        return self._credit_apply_no

    @credit_apply_no.setter
    def credit_apply_no(self, value):
        self._credit_apply_no = value
    @property
    def credit_apply_result(self):
        return self._credit_apply_result

    @credit_apply_result.setter
    def credit_apply_result(self, value):
        if isinstance(value, HonorCreditApplyResultDTO):
            self._credit_apply_result = value
        else:
            self._credit_apply_result = HonorCreditApplyResultDTO.from_alipay_dict(value)
    @property
    def lend_result(self):
        return self._lend_result

    @lend_result.setter
    def lend_result(self, value):
        if isinstance(value, HonorLendApplyResultDTO):
            self._lend_result = value
        else:
            self._lend_result = HonorLendApplyResultDTO.from_alipay_dict(value)
    @property
    def logoff_result(self):
        return self._logoff_result

    @logoff_result.setter
    def logoff_result(self, value):
        if isinstance(value, HonorLogoffResultDTO):
            self._logoff_result = value
        else:
            self._logoff_result = HonorLogoffResultDTO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def repay_result(self):
        return self._repay_result

    @repay_result.setter
    def repay_result(self, value):
        if isinstance(value, HonorRepayApplyResultDTO):
            self._repay_result = value
        else:
            self._repay_result = HonorRepayApplyResultDTO.from_alipay_dict(value)
    @property
    def unifygw_result(self):
        return self._unifygw_result

    @unifygw_result.setter
    def unifygw_result(self, value):
        if isinstance(value, HonorUnifygwCommonResult):
            self._unifygw_result = value
        else:
            self._unifygw_result = HonorUnifygwCommonResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.coupon_send_result:
            if hasattr(self.coupon_send_result, 'to_alipay_dict'):
                params['coupon_send_result'] = self.coupon_send_result.to_alipay_dict()
            else:
                params['coupon_send_result'] = self.coupon_send_result
        if self.credit_apply_no:
            if hasattr(self.credit_apply_no, 'to_alipay_dict'):
                params['credit_apply_no'] = self.credit_apply_no.to_alipay_dict()
            else:
                params['credit_apply_no'] = self.credit_apply_no
        if self.credit_apply_result:
            if hasattr(self.credit_apply_result, 'to_alipay_dict'):
                params['credit_apply_result'] = self.credit_apply_result.to_alipay_dict()
            else:
                params['credit_apply_result'] = self.credit_apply_result
        if self.lend_result:
            if hasattr(self.lend_result, 'to_alipay_dict'):
                params['lend_result'] = self.lend_result.to_alipay_dict()
            else:
                params['lend_result'] = self.lend_result
        if self.logoff_result:
            if hasattr(self.logoff_result, 'to_alipay_dict'):
                params['logoff_result'] = self.logoff_result.to_alipay_dict()
            else:
                params['logoff_result'] = self.logoff_result
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.repay_result:
            if hasattr(self.repay_result, 'to_alipay_dict'):
                params['repay_result'] = self.repay_result.to_alipay_dict()
            else:
                params['repay_result'] = self.repay_result
        if self.unifygw_result:
            if hasattr(self.unifygw_result, 'to_alipay_dict'):
                params['unifygw_result'] = self.unifygw_result.to_alipay_dict()
            else:
                params['unifygw_result'] = self.unifygw_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorOpenapitestQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'coupon_send_result' in d:
            o.coupon_send_result = d['coupon_send_result']
        if 'credit_apply_no' in d:
            o.credit_apply_no = d['credit_apply_no']
        if 'credit_apply_result' in d:
            o.credit_apply_result = d['credit_apply_result']
        if 'lend_result' in d:
            o.lend_result = d['lend_result']
        if 'logoff_result' in d:
            o.logoff_result = d['logoff_result']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'repay_result' in d:
            o.repay_result = d['repay_result']
        if 'unifygw_result' in d:
            o.unifygw_result = d['unifygw_result']
        return o


