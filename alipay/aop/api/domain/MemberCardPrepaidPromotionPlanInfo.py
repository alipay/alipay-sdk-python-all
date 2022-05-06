#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberCardVoucherBenefitInfo import MemberCardVoucherBenefitInfo


class MemberCardPrepaidPromotionPlanInfo(object):

    def __init__(self):
        self._benefit = None
        self._benefit_voucher_list = None
        self._create_time = None
        self._end_time = None
        self._modify_time = None
        self._principal = None
        self._promotion_plan_id = None
        self._publish_total_num = None
        self._publish_total_remain_num = None
        self._start_time = None
        self._status = None

    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def benefit_voucher_list(self):
        return self._benefit_voucher_list

    @benefit_voucher_list.setter
    def benefit_voucher_list(self, value):
        if isinstance(value, MemberCardVoucherBenefitInfo):
            self._benefit_voucher_list = value
        else:
            self._benefit_voucher_list = MemberCardVoucherBenefitInfo.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def promotion_plan_id(self):
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, value):
        self._promotion_plan_id = value
    @property
    def publish_total_num(self):
        return self._publish_total_num

    @publish_total_num.setter
    def publish_total_num(self, value):
        self._publish_total_num = value
    @property
    def publish_total_remain_num(self):
        return self._publish_total_remain_num

    @publish_total_remain_num.setter
    def publish_total_remain_num(self, value):
        self._publish_total_remain_num = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.benefit_voucher_list:
            if hasattr(self.benefit_voucher_list, 'to_alipay_dict'):
                params['benefit_voucher_list'] = self.benefit_voucher_list.to_alipay_dict()
            else:
                params['benefit_voucher_list'] = self.benefit_voucher_list
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.promotion_plan_id:
            if hasattr(self.promotion_plan_id, 'to_alipay_dict'):
                params['promotion_plan_id'] = self.promotion_plan_id.to_alipay_dict()
            else:
                params['promotion_plan_id'] = self.promotion_plan_id
        if self.publish_total_num:
            if hasattr(self.publish_total_num, 'to_alipay_dict'):
                params['publish_total_num'] = self.publish_total_num.to_alipay_dict()
            else:
                params['publish_total_num'] = self.publish_total_num
        if self.publish_total_remain_num:
            if hasattr(self.publish_total_remain_num, 'to_alipay_dict'):
                params['publish_total_remain_num'] = self.publish_total_remain_num.to_alipay_dict()
            else:
                params['publish_total_remain_num'] = self.publish_total_remain_num
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardPrepaidPromotionPlanInfo()
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'benefit_voucher_list' in d:
            o.benefit_voucher_list = d['benefit_voucher_list']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'principal' in d:
            o.principal = d['principal']
        if 'promotion_plan_id' in d:
            o.promotion_plan_id = d['promotion_plan_id']
        if 'publish_total_num' in d:
            o.publish_total_num = d['publish_total_num']
        if 'publish_total_remain_num' in d:
            o.publish_total_remain_num = d['publish_total_remain_num']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


