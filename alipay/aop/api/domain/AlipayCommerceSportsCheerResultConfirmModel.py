#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsCheerResultConfirmModel(object):

    def __init__(self):
        self._game_serial_number = None
        self._is_success = None
        self._other_team_score = None
        self._user_team_score = None

    @property
    def game_serial_number(self):
        return self._game_serial_number

    @game_serial_number.setter
    def game_serial_number(self, value):
        self._game_serial_number = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def other_team_score(self):
        return self._other_team_score

    @other_team_score.setter
    def other_team_score(self, value):
        self._other_team_score = value
    @property
    def user_team_score(self):
        return self._user_team_score

    @user_team_score.setter
    def user_team_score(self, value):
        self._user_team_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.game_serial_number:
            if hasattr(self.game_serial_number, 'to_alipay_dict'):
                params['game_serial_number'] = self.game_serial_number.to_alipay_dict()
            else:
                params['game_serial_number'] = self.game_serial_number
        if self.is_success:
            if hasattr(self.is_success, 'to_alipay_dict'):
                params['is_success'] = self.is_success.to_alipay_dict()
            else:
                params['is_success'] = self.is_success
        if self.other_team_score:
            if hasattr(self.other_team_score, 'to_alipay_dict'):
                params['other_team_score'] = self.other_team_score.to_alipay_dict()
            else:
                params['other_team_score'] = self.other_team_score
        if self.user_team_score:
            if hasattr(self.user_team_score, 'to_alipay_dict'):
                params['user_team_score'] = self.user_team_score.to_alipay_dict()
            else:
                params['user_team_score'] = self.user_team_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsCheerResultConfirmModel()
        if 'game_serial_number' in d:
            o.game_serial_number = d['game_serial_number']
        if 'is_success' in d:
            o.is_success = d['is_success']
        if 'other_team_score' in d:
            o.other_team_score = d['other_team_score']
        if 'user_team_score' in d:
            o.user_team_score = d['user_team_score']
        return o


