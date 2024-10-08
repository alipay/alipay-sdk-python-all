#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Satisfaction(object):

    def __init__(self):
        self._agent_alipay_uid = None
        self._agent_new_old_type = None
        self._agent_nickname = None
        self._agent_real_name = None
        self._agent_skill_group = None
        self._ai_assistant_score = None
        self._appraise_id = None
        self._appraise_question_cnt = None
        self._appraise_result = None
        self._appraise_trigger_time = None
        self._appraise_type_name = None
        self._avg_response_length = None
        self._business_name = None
        self._business_name_level_2 = None
        self._call_in_user_type = None
        self._cat_name_level_1 = None
        self._cat_name_level_2 = None
        self._cat_name_level_3 = None
        self._close_case_length = None
        self._close_ticket_type = None
        self._entry_difficulty_score = None
        self._first_response_length = None
        self._grasp_score = None
        self._is_discontinue = None
        self._is_solved = None
        self._is_submitted = None
        self._manual_service_score = None
        self._order_id = None
        self._origin_session_id_ant = None
        self._other_adv = None
        self._overall_score = None
        self._process_speed_score = None
        self._queue_length = None
        self._report_date = None
        self._self_service_score = None
        self._service_attitude_score = None
        self._service_channel = None
        self._session_id_ant = None
        self._session_id_hello = None
        self._session_type = None
        self._solution_score = None
        self._sub_channel = None
        self._user_guid = None
        self._user_phone = None

    @property
    def agent_alipay_uid(self):
        return self._agent_alipay_uid

    @agent_alipay_uid.setter
    def agent_alipay_uid(self, value):
        self._agent_alipay_uid = value
    @property
    def agent_new_old_type(self):
        return self._agent_new_old_type

    @agent_new_old_type.setter
    def agent_new_old_type(self, value):
        self._agent_new_old_type = value
    @property
    def agent_nickname(self):
        return self._agent_nickname

    @agent_nickname.setter
    def agent_nickname(self, value):
        self._agent_nickname = value
    @property
    def agent_real_name(self):
        return self._agent_real_name

    @agent_real_name.setter
    def agent_real_name(self, value):
        self._agent_real_name = value
    @property
    def agent_skill_group(self):
        return self._agent_skill_group

    @agent_skill_group.setter
    def agent_skill_group(self, value):
        self._agent_skill_group = value
    @property
    def ai_assistant_score(self):
        return self._ai_assistant_score

    @ai_assistant_score.setter
    def ai_assistant_score(self, value):
        self._ai_assistant_score = value
    @property
    def appraise_id(self):
        return self._appraise_id

    @appraise_id.setter
    def appraise_id(self, value):
        self._appraise_id = value
    @property
    def appraise_question_cnt(self):
        return self._appraise_question_cnt

    @appraise_question_cnt.setter
    def appraise_question_cnt(self, value):
        self._appraise_question_cnt = value
    @property
    def appraise_result(self):
        return self._appraise_result

    @appraise_result.setter
    def appraise_result(self, value):
        self._appraise_result = value
    @property
    def appraise_trigger_time(self):
        return self._appraise_trigger_time

    @appraise_trigger_time.setter
    def appraise_trigger_time(self, value):
        self._appraise_trigger_time = value
    @property
    def appraise_type_name(self):
        return self._appraise_type_name

    @appraise_type_name.setter
    def appraise_type_name(self, value):
        self._appraise_type_name = value
    @property
    def avg_response_length(self):
        return self._avg_response_length

    @avg_response_length.setter
    def avg_response_length(self, value):
        self._avg_response_length = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def business_name_level_2(self):
        return self._business_name_level_2

    @business_name_level_2.setter
    def business_name_level_2(self, value):
        self._business_name_level_2 = value
    @property
    def call_in_user_type(self):
        return self._call_in_user_type

    @call_in_user_type.setter
    def call_in_user_type(self, value):
        self._call_in_user_type = value
    @property
    def cat_name_level_1(self):
        return self._cat_name_level_1

    @cat_name_level_1.setter
    def cat_name_level_1(self, value):
        self._cat_name_level_1 = value
    @property
    def cat_name_level_2(self):
        return self._cat_name_level_2

    @cat_name_level_2.setter
    def cat_name_level_2(self, value):
        self._cat_name_level_2 = value
    @property
    def cat_name_level_3(self):
        return self._cat_name_level_3

    @cat_name_level_3.setter
    def cat_name_level_3(self, value):
        self._cat_name_level_3 = value
    @property
    def close_case_length(self):
        return self._close_case_length

    @close_case_length.setter
    def close_case_length(self, value):
        self._close_case_length = value
    @property
    def close_ticket_type(self):
        return self._close_ticket_type

    @close_ticket_type.setter
    def close_ticket_type(self, value):
        self._close_ticket_type = value
    @property
    def entry_difficulty_score(self):
        return self._entry_difficulty_score

    @entry_difficulty_score.setter
    def entry_difficulty_score(self, value):
        self._entry_difficulty_score = value
    @property
    def first_response_length(self):
        return self._first_response_length

    @first_response_length.setter
    def first_response_length(self, value):
        self._first_response_length = value
    @property
    def grasp_score(self):
        return self._grasp_score

    @grasp_score.setter
    def grasp_score(self, value):
        self._grasp_score = value
    @property
    def is_discontinue(self):
        return self._is_discontinue

    @is_discontinue.setter
    def is_discontinue(self, value):
        self._is_discontinue = value
    @property
    def is_solved(self):
        return self._is_solved

    @is_solved.setter
    def is_solved(self, value):
        self._is_solved = value
    @property
    def is_submitted(self):
        return self._is_submitted

    @is_submitted.setter
    def is_submitted(self, value):
        self._is_submitted = value
    @property
    def manual_service_score(self):
        return self._manual_service_score

    @manual_service_score.setter
    def manual_service_score(self, value):
        self._manual_service_score = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def origin_session_id_ant(self):
        return self._origin_session_id_ant

    @origin_session_id_ant.setter
    def origin_session_id_ant(self, value):
        self._origin_session_id_ant = value
    @property
    def other_adv(self):
        return self._other_adv

    @other_adv.setter
    def other_adv(self, value):
        self._other_adv = value
    @property
    def overall_score(self):
        return self._overall_score

    @overall_score.setter
    def overall_score(self, value):
        self._overall_score = value
    @property
    def process_speed_score(self):
        return self._process_speed_score

    @process_speed_score.setter
    def process_speed_score(self, value):
        self._process_speed_score = value
    @property
    def queue_length(self):
        return self._queue_length

    @queue_length.setter
    def queue_length(self, value):
        self._queue_length = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def self_service_score(self):
        return self._self_service_score

    @self_service_score.setter
    def self_service_score(self, value):
        self._self_service_score = value
    @property
    def service_attitude_score(self):
        return self._service_attitude_score

    @service_attitude_score.setter
    def service_attitude_score(self, value):
        self._service_attitude_score = value
    @property
    def service_channel(self):
        return self._service_channel

    @service_channel.setter
    def service_channel(self, value):
        self._service_channel = value
    @property
    def session_id_ant(self):
        return self._session_id_ant

    @session_id_ant.setter
    def session_id_ant(self, value):
        self._session_id_ant = value
    @property
    def session_id_hello(self):
        return self._session_id_hello

    @session_id_hello.setter
    def session_id_hello(self, value):
        self._session_id_hello = value
    @property
    def session_type(self):
        return self._session_type

    @session_type.setter
    def session_type(self, value):
        self._session_type = value
    @property
    def solution_score(self):
        return self._solution_score

    @solution_score.setter
    def solution_score(self, value):
        self._solution_score = value
    @property
    def sub_channel(self):
        return self._sub_channel

    @sub_channel.setter
    def sub_channel(self, value):
        self._sub_channel = value
    @property
    def user_guid(self):
        return self._user_guid

    @user_guid.setter
    def user_guid(self, value):
        self._user_guid = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_alipay_uid:
            if hasattr(self.agent_alipay_uid, 'to_alipay_dict'):
                params['agent_alipay_uid'] = self.agent_alipay_uid.to_alipay_dict()
            else:
                params['agent_alipay_uid'] = self.agent_alipay_uid
        if self.agent_new_old_type:
            if hasattr(self.agent_new_old_type, 'to_alipay_dict'):
                params['agent_new_old_type'] = self.agent_new_old_type.to_alipay_dict()
            else:
                params['agent_new_old_type'] = self.agent_new_old_type
        if self.agent_nickname:
            if hasattr(self.agent_nickname, 'to_alipay_dict'):
                params['agent_nickname'] = self.agent_nickname.to_alipay_dict()
            else:
                params['agent_nickname'] = self.agent_nickname
        if self.agent_real_name:
            if hasattr(self.agent_real_name, 'to_alipay_dict'):
                params['agent_real_name'] = self.agent_real_name.to_alipay_dict()
            else:
                params['agent_real_name'] = self.agent_real_name
        if self.agent_skill_group:
            if hasattr(self.agent_skill_group, 'to_alipay_dict'):
                params['agent_skill_group'] = self.agent_skill_group.to_alipay_dict()
            else:
                params['agent_skill_group'] = self.agent_skill_group
        if self.ai_assistant_score:
            if hasattr(self.ai_assistant_score, 'to_alipay_dict'):
                params['ai_assistant_score'] = self.ai_assistant_score.to_alipay_dict()
            else:
                params['ai_assistant_score'] = self.ai_assistant_score
        if self.appraise_id:
            if hasattr(self.appraise_id, 'to_alipay_dict'):
                params['appraise_id'] = self.appraise_id.to_alipay_dict()
            else:
                params['appraise_id'] = self.appraise_id
        if self.appraise_question_cnt:
            if hasattr(self.appraise_question_cnt, 'to_alipay_dict'):
                params['appraise_question_cnt'] = self.appraise_question_cnt.to_alipay_dict()
            else:
                params['appraise_question_cnt'] = self.appraise_question_cnt
        if self.appraise_result:
            if hasattr(self.appraise_result, 'to_alipay_dict'):
                params['appraise_result'] = self.appraise_result.to_alipay_dict()
            else:
                params['appraise_result'] = self.appraise_result
        if self.appraise_trigger_time:
            if hasattr(self.appraise_trigger_time, 'to_alipay_dict'):
                params['appraise_trigger_time'] = self.appraise_trigger_time.to_alipay_dict()
            else:
                params['appraise_trigger_time'] = self.appraise_trigger_time
        if self.appraise_type_name:
            if hasattr(self.appraise_type_name, 'to_alipay_dict'):
                params['appraise_type_name'] = self.appraise_type_name.to_alipay_dict()
            else:
                params['appraise_type_name'] = self.appraise_type_name
        if self.avg_response_length:
            if hasattr(self.avg_response_length, 'to_alipay_dict'):
                params['avg_response_length'] = self.avg_response_length.to_alipay_dict()
            else:
                params['avg_response_length'] = self.avg_response_length
        if self.business_name:
            if hasattr(self.business_name, 'to_alipay_dict'):
                params['business_name'] = self.business_name.to_alipay_dict()
            else:
                params['business_name'] = self.business_name
        if self.business_name_level_2:
            if hasattr(self.business_name_level_2, 'to_alipay_dict'):
                params['business_name_level_2'] = self.business_name_level_2.to_alipay_dict()
            else:
                params['business_name_level_2'] = self.business_name_level_2
        if self.call_in_user_type:
            if hasattr(self.call_in_user_type, 'to_alipay_dict'):
                params['call_in_user_type'] = self.call_in_user_type.to_alipay_dict()
            else:
                params['call_in_user_type'] = self.call_in_user_type
        if self.cat_name_level_1:
            if hasattr(self.cat_name_level_1, 'to_alipay_dict'):
                params['cat_name_level_1'] = self.cat_name_level_1.to_alipay_dict()
            else:
                params['cat_name_level_1'] = self.cat_name_level_1
        if self.cat_name_level_2:
            if hasattr(self.cat_name_level_2, 'to_alipay_dict'):
                params['cat_name_level_2'] = self.cat_name_level_2.to_alipay_dict()
            else:
                params['cat_name_level_2'] = self.cat_name_level_2
        if self.cat_name_level_3:
            if hasattr(self.cat_name_level_3, 'to_alipay_dict'):
                params['cat_name_level_3'] = self.cat_name_level_3.to_alipay_dict()
            else:
                params['cat_name_level_3'] = self.cat_name_level_3
        if self.close_case_length:
            if hasattr(self.close_case_length, 'to_alipay_dict'):
                params['close_case_length'] = self.close_case_length.to_alipay_dict()
            else:
                params['close_case_length'] = self.close_case_length
        if self.close_ticket_type:
            if hasattr(self.close_ticket_type, 'to_alipay_dict'):
                params['close_ticket_type'] = self.close_ticket_type.to_alipay_dict()
            else:
                params['close_ticket_type'] = self.close_ticket_type
        if self.entry_difficulty_score:
            if hasattr(self.entry_difficulty_score, 'to_alipay_dict'):
                params['entry_difficulty_score'] = self.entry_difficulty_score.to_alipay_dict()
            else:
                params['entry_difficulty_score'] = self.entry_difficulty_score
        if self.first_response_length:
            if hasattr(self.first_response_length, 'to_alipay_dict'):
                params['first_response_length'] = self.first_response_length.to_alipay_dict()
            else:
                params['first_response_length'] = self.first_response_length
        if self.grasp_score:
            if hasattr(self.grasp_score, 'to_alipay_dict'):
                params['grasp_score'] = self.grasp_score.to_alipay_dict()
            else:
                params['grasp_score'] = self.grasp_score
        if self.is_discontinue:
            if hasattr(self.is_discontinue, 'to_alipay_dict'):
                params['is_discontinue'] = self.is_discontinue.to_alipay_dict()
            else:
                params['is_discontinue'] = self.is_discontinue
        if self.is_solved:
            if hasattr(self.is_solved, 'to_alipay_dict'):
                params['is_solved'] = self.is_solved.to_alipay_dict()
            else:
                params['is_solved'] = self.is_solved
        if self.is_submitted:
            if hasattr(self.is_submitted, 'to_alipay_dict'):
                params['is_submitted'] = self.is_submitted.to_alipay_dict()
            else:
                params['is_submitted'] = self.is_submitted
        if self.manual_service_score:
            if hasattr(self.manual_service_score, 'to_alipay_dict'):
                params['manual_service_score'] = self.manual_service_score.to_alipay_dict()
            else:
                params['manual_service_score'] = self.manual_service_score
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.origin_session_id_ant:
            if hasattr(self.origin_session_id_ant, 'to_alipay_dict'):
                params['origin_session_id_ant'] = self.origin_session_id_ant.to_alipay_dict()
            else:
                params['origin_session_id_ant'] = self.origin_session_id_ant
        if self.other_adv:
            if hasattr(self.other_adv, 'to_alipay_dict'):
                params['other_adv'] = self.other_adv.to_alipay_dict()
            else:
                params['other_adv'] = self.other_adv
        if self.overall_score:
            if hasattr(self.overall_score, 'to_alipay_dict'):
                params['overall_score'] = self.overall_score.to_alipay_dict()
            else:
                params['overall_score'] = self.overall_score
        if self.process_speed_score:
            if hasattr(self.process_speed_score, 'to_alipay_dict'):
                params['process_speed_score'] = self.process_speed_score.to_alipay_dict()
            else:
                params['process_speed_score'] = self.process_speed_score
        if self.queue_length:
            if hasattr(self.queue_length, 'to_alipay_dict'):
                params['queue_length'] = self.queue_length.to_alipay_dict()
            else:
                params['queue_length'] = self.queue_length
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.self_service_score:
            if hasattr(self.self_service_score, 'to_alipay_dict'):
                params['self_service_score'] = self.self_service_score.to_alipay_dict()
            else:
                params['self_service_score'] = self.self_service_score
        if self.service_attitude_score:
            if hasattr(self.service_attitude_score, 'to_alipay_dict'):
                params['service_attitude_score'] = self.service_attitude_score.to_alipay_dict()
            else:
                params['service_attitude_score'] = self.service_attitude_score
        if self.service_channel:
            if hasattr(self.service_channel, 'to_alipay_dict'):
                params['service_channel'] = self.service_channel.to_alipay_dict()
            else:
                params['service_channel'] = self.service_channel
        if self.session_id_ant:
            if hasattr(self.session_id_ant, 'to_alipay_dict'):
                params['session_id_ant'] = self.session_id_ant.to_alipay_dict()
            else:
                params['session_id_ant'] = self.session_id_ant
        if self.session_id_hello:
            if hasattr(self.session_id_hello, 'to_alipay_dict'):
                params['session_id_hello'] = self.session_id_hello.to_alipay_dict()
            else:
                params['session_id_hello'] = self.session_id_hello
        if self.session_type:
            if hasattr(self.session_type, 'to_alipay_dict'):
                params['session_type'] = self.session_type.to_alipay_dict()
            else:
                params['session_type'] = self.session_type
        if self.solution_score:
            if hasattr(self.solution_score, 'to_alipay_dict'):
                params['solution_score'] = self.solution_score.to_alipay_dict()
            else:
                params['solution_score'] = self.solution_score
        if self.sub_channel:
            if hasattr(self.sub_channel, 'to_alipay_dict'):
                params['sub_channel'] = self.sub_channel.to_alipay_dict()
            else:
                params['sub_channel'] = self.sub_channel
        if self.user_guid:
            if hasattr(self.user_guid, 'to_alipay_dict'):
                params['user_guid'] = self.user_guid.to_alipay_dict()
            else:
                params['user_guid'] = self.user_guid
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Satisfaction()
        if 'agent_alipay_uid' in d:
            o.agent_alipay_uid = d['agent_alipay_uid']
        if 'agent_new_old_type' in d:
            o.agent_new_old_type = d['agent_new_old_type']
        if 'agent_nickname' in d:
            o.agent_nickname = d['agent_nickname']
        if 'agent_real_name' in d:
            o.agent_real_name = d['agent_real_name']
        if 'agent_skill_group' in d:
            o.agent_skill_group = d['agent_skill_group']
        if 'ai_assistant_score' in d:
            o.ai_assistant_score = d['ai_assistant_score']
        if 'appraise_id' in d:
            o.appraise_id = d['appraise_id']
        if 'appraise_question_cnt' in d:
            o.appraise_question_cnt = d['appraise_question_cnt']
        if 'appraise_result' in d:
            o.appraise_result = d['appraise_result']
        if 'appraise_trigger_time' in d:
            o.appraise_trigger_time = d['appraise_trigger_time']
        if 'appraise_type_name' in d:
            o.appraise_type_name = d['appraise_type_name']
        if 'avg_response_length' in d:
            o.avg_response_length = d['avg_response_length']
        if 'business_name' in d:
            o.business_name = d['business_name']
        if 'business_name_level_2' in d:
            o.business_name_level_2 = d['business_name_level_2']
        if 'call_in_user_type' in d:
            o.call_in_user_type = d['call_in_user_type']
        if 'cat_name_level_1' in d:
            o.cat_name_level_1 = d['cat_name_level_1']
        if 'cat_name_level_2' in d:
            o.cat_name_level_2 = d['cat_name_level_2']
        if 'cat_name_level_3' in d:
            o.cat_name_level_3 = d['cat_name_level_3']
        if 'close_case_length' in d:
            o.close_case_length = d['close_case_length']
        if 'close_ticket_type' in d:
            o.close_ticket_type = d['close_ticket_type']
        if 'entry_difficulty_score' in d:
            o.entry_difficulty_score = d['entry_difficulty_score']
        if 'first_response_length' in d:
            o.first_response_length = d['first_response_length']
        if 'grasp_score' in d:
            o.grasp_score = d['grasp_score']
        if 'is_discontinue' in d:
            o.is_discontinue = d['is_discontinue']
        if 'is_solved' in d:
            o.is_solved = d['is_solved']
        if 'is_submitted' in d:
            o.is_submitted = d['is_submitted']
        if 'manual_service_score' in d:
            o.manual_service_score = d['manual_service_score']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'origin_session_id_ant' in d:
            o.origin_session_id_ant = d['origin_session_id_ant']
        if 'other_adv' in d:
            o.other_adv = d['other_adv']
        if 'overall_score' in d:
            o.overall_score = d['overall_score']
        if 'process_speed_score' in d:
            o.process_speed_score = d['process_speed_score']
        if 'queue_length' in d:
            o.queue_length = d['queue_length']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'self_service_score' in d:
            o.self_service_score = d['self_service_score']
        if 'service_attitude_score' in d:
            o.service_attitude_score = d['service_attitude_score']
        if 'service_channel' in d:
            o.service_channel = d['service_channel']
        if 'session_id_ant' in d:
            o.session_id_ant = d['session_id_ant']
        if 'session_id_hello' in d:
            o.session_id_hello = d['session_id_hello']
        if 'session_type' in d:
            o.session_type = d['session_type']
        if 'solution_score' in d:
            o.solution_score = d['solution_score']
        if 'sub_channel' in d:
            o.sub_channel = d['sub_channel']
        if 'user_guid' in d:
            o.user_guid = d['user_guid']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


