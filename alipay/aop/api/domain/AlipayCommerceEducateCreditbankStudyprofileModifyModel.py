#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditBankCertificateExperience import CreditBankCertificateExperience
from alipay.aop.api.domain.CreditBankCredit import CreditBankCredit
from alipay.aop.api.domain.CreditBankTraining import CreditBankTraining


class AlipayCommerceEducateCreditbankStudyprofileModifyModel(object):

    def __init__(self):
        self._cb_id = None
        self._certificate_experience = None
        self._certificate_num = None
        self._channel = None
        self._credit = None
        self._credit_num = None
        self._training = None
        self._training_num = None
        self._user_id = None

    @property
    def cb_id(self):
        return self._cb_id

    @cb_id.setter
    def cb_id(self, value):
        self._cb_id = value
    @property
    def certificate_experience(self):
        return self._certificate_experience

    @certificate_experience.setter
    def certificate_experience(self, value):
        if isinstance(value, list):
            self._certificate_experience = list()
            for i in value:
                if isinstance(i, CreditBankCertificateExperience):
                    self._certificate_experience.append(i)
                else:
                    self._certificate_experience.append(CreditBankCertificateExperience.from_alipay_dict(i))
    @property
    def certificate_num(self):
        return self._certificate_num

    @certificate_num.setter
    def certificate_num(self, value):
        self._certificate_num = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, value):
        if isinstance(value, list):
            self._credit = list()
            for i in value:
                if isinstance(i, CreditBankCredit):
                    self._credit.append(i)
                else:
                    self._credit.append(CreditBankCredit.from_alipay_dict(i))
    @property
    def credit_num(self):
        return self._credit_num

    @credit_num.setter
    def credit_num(self, value):
        self._credit_num = value
    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, value):
        if isinstance(value, list):
            self._training = list()
            for i in value:
                if isinstance(i, CreditBankTraining):
                    self._training.append(i)
                else:
                    self._training.append(CreditBankTraining.from_alipay_dict(i))
    @property
    def training_num(self):
        return self._training_num

    @training_num.setter
    def training_num(self, value):
        self._training_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cb_id:
            if hasattr(self.cb_id, 'to_alipay_dict'):
                params['cb_id'] = self.cb_id.to_alipay_dict()
            else:
                params['cb_id'] = self.cb_id
        if self.certificate_experience:
            if isinstance(self.certificate_experience, list):
                for i in range(0, len(self.certificate_experience)):
                    element = self.certificate_experience[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_experience[i] = element.to_alipay_dict()
            if hasattr(self.certificate_experience, 'to_alipay_dict'):
                params['certificate_experience'] = self.certificate_experience.to_alipay_dict()
            else:
                params['certificate_experience'] = self.certificate_experience
        if self.certificate_num:
            if hasattr(self.certificate_num, 'to_alipay_dict'):
                params['certificate_num'] = self.certificate_num.to_alipay_dict()
            else:
                params['certificate_num'] = self.certificate_num
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.credit:
            if isinstance(self.credit, list):
                for i in range(0, len(self.credit)):
                    element = self.credit[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit[i] = element.to_alipay_dict()
            if hasattr(self.credit, 'to_alipay_dict'):
                params['credit'] = self.credit.to_alipay_dict()
            else:
                params['credit'] = self.credit
        if self.credit_num:
            if hasattr(self.credit_num, 'to_alipay_dict'):
                params['credit_num'] = self.credit_num.to_alipay_dict()
            else:
                params['credit_num'] = self.credit_num
        if self.training:
            if isinstance(self.training, list):
                for i in range(0, len(self.training)):
                    element = self.training[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.training[i] = element.to_alipay_dict()
            if hasattr(self.training, 'to_alipay_dict'):
                params['training'] = self.training.to_alipay_dict()
            else:
                params['training'] = self.training
        if self.training_num:
            if hasattr(self.training_num, 'to_alipay_dict'):
                params['training_num'] = self.training_num.to_alipay_dict()
            else:
                params['training_num'] = self.training_num
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
        o = AlipayCommerceEducateCreditbankStudyprofileModifyModel()
        if 'cb_id' in d:
            o.cb_id = d['cb_id']
        if 'certificate_experience' in d:
            o.certificate_experience = d['certificate_experience']
        if 'certificate_num' in d:
            o.certificate_num = d['certificate_num']
        if 'channel' in d:
            o.channel = d['channel']
        if 'credit' in d:
            o.credit = d['credit']
        if 'credit_num' in d:
            o.credit_num = d['credit_num']
        if 'training' in d:
            o.training = d['training']
        if 'training_num' in d:
            o.training_num = d['training_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


