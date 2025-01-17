# ThermIQ generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4
FIELD_BITMASK = 3


# Register as sensors
reg_id = {
#  reg_id          : ['reg#' ],
  'outdoor_t'                    : ['r00', 'temperature',            'ºC',                           ],
  'indoor_t'                     : ['r01', 'temperature',            'ºC',                           ],
  'indoor_dec_t'                 : ['r02', 'temperature',            '0.1C',                          ],
  'indoor_target_t'              : ['r03', 'temperature',            'ºC',                           ],
  'indoor_target_dec_t'          : ['r04', 'temperature',            '0.1C',                          ],
  'supplyline_t'                 : ['r05', 'temperature',            'ºC',                           ],
  'returnline_t'                 : ['r06', 'temperature',            'ºC',                           ],
  'boiler_t'                     : ['r07', 'temperature',            'ºC',                           ],
  'brine_out_t'                  : ['r08', 'temperature',            'ºC',                           ],
  'brine_in_t'                   : ['r09', 'temperature',            'ºC',                           ],
  'cooling_t'                    : ['r0a', 'temperature',            'ºC',                           ],
  'supply_shunt_t'               : ['r0b', 'temperature',            'ºC',                           ],
  'current_consumed_a'           : ['r0c', 'sensor',                 'A',                             ],
  'boiler_3kw_on'                : ['r0d', 'binary_sensor',          'A',            0x0001           ],
  'boiler_6kw_on'                : ['r0d', 'binary_sensor',          'A',            0x0002           ],
  'supplyline_target_t'          : ['r0e', 'temperature',            'ºC',                           ],
  'supplyline_shunt_target_t'    : ['r0f', 'temperature',            'ºC',                           ],
  'brine_pump_on'                : ['r10', 'binary_sensor',          'ºC',          0x0001           ],
  'compressor_on'                : ['r10', 'binary_sensor',          'ºC',          0x0002           ],
  'supply_pump_on'               : ['r10', 'binary_sensor',          'ºC',          0x0004           ],
  'hotwaterproduction_on'        : ['r10', 'binary_sensor',          'ºC',          0x0008           ],
  'aux2_heating_on'              : ['r10', 'binary_sensor',          'ºC',          0x0010           ],
  'shunt1_n'                     : ['r10', 'binary_sensor',          'ºC',          0x0020           ],
  'shunt1_p'                     : ['r10', 'binary_sensor',          'ºC',          0x0040           ],
  'aux1_heating_on'              : ['r10', 'binary_sensor',          'ºC',          0x0080           ],
  'shunt2_n'                     : ['r11', 'binary_sensor',          'ºC',          0x0001           ],
  'shunt2_p'                     : ['r11', 'binary_sensor',          'ºC',          0x0002           ],
  'shount_cooling_n'             : ['r11', 'binary_sensor',          'ºC',          0x0004           ],
  'shount_cooling_p'             : ['r11', 'binary_sensor',          'ºC',          0x0008           ],
  'active_cooling_on'            : ['r11', 'binary_sensor',          'ºC',          0x0010           ],
  'passive_cooling_on'           : ['r11', 'binary_sensor',          'ºC',          0x0020           ],
  'alarm_indication_on'          : ['r11', 'binary_sensor',          'ºC',          0x0040           ],
  'pwm_out_period'               : ['r12', 'sensor',                 '%',                             ],
  'highpreassure_alm'            : ['r13', 'binary_sensor',          '%',            0x0001           ],
  'lowpreassure_alm'             : ['r13', 'binary_sensor',          '%',            0x0002           ],
  'motorbreaker_alm'             : ['r13', 'binary_sensor',          '%',            0x0004           ],
  'brine_flow_alm'               : ['r13', 'binary_sensor',          '%',            0x0008           ],
  'bine_temperature_alm'         : ['r13', 'binary_sensor',          '%',            0x0010           ],
  'outdoor_sensor_alm'           : ['r14', 'binary_sensor',          '%',            0x0001           ],
  'supplyline_sensor_alm'        : ['r14', 'binary_sensor',          '%',            0x0002           ],
  'returnline_sensor_alm'        : ['r14', 'binary_sensor',          '%',            0x0004           ],
  'boiler_sensor_alm'            : ['r14', 'binary_sensor',          '%',            0x0008           ],
  'indoor_sensor_alm'            : ['r14', 'binary_sensor',          '%',            0x0010           ],
  'phase_order_alm'              : ['r14', 'binary_sensor',          '%',            0x0020           ],
  'overheating_alm'              : ['r14', 'binary_sensor',          '%',            0x0040           ],
  'demand1'                      : ['r15', 'sensor',                 '',                              ],
  'demand2'                      : ['r16', 'sensor',                 '',                              ],
  'pressurepipe_t'               : ['r17', 'temperature',            'ºC',                           ],
  'hgw_water_t'                  : ['r18', 'temperature',            'ºC',                           ],
  'integral1'                    : ['r19', 'sensor',                 'Cmin',                          ],
  'integral1_a_limit'            : ['r1a', 'sensor',                 '',                              ],
  'defrost_time_m'               : ['r1b', 'time',                   '*10s',                          ],
  'time_to_start_min_m'          : ['r1c', 'time',                   'min',                           ],
  'sw_version'                   : ['r1d', 'sensor',                 '',                              ],
  'supply_pump_speed'            : ['r1e', 'sensor',                 '%',                             ],
  'brine_pump_speed'             : ['r1f', 'sensor',                 '%',                             ],
  'status3_m'                    : ['r20', 'sensor',                 '',                              ],
  'indoor_requested_t'           : ['r32', 'temperature_input',      'ºC',               0,     50   ],
  'main_mode'                    : ['r33', 'select_input',           'mode',              0,     16   ],
  'integral1_curve_slope'        : ['r34', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_min'          : ['r35', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_max'          : ['r36', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_p5'           : ['r37', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_0'            : ['r38', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_n5'           : ['r39', 'temperature_input',      'ºC',               0,    200   ],
  'heating_stop_t'               : ['r3a', 'temperature_input',      'ºC',               0,    200   ],
  'reduction_t'                  : ['r3b', 'temperature_input',      'ºC',               0,    100   ],
  'room_factor'                  : ['r3c', 'temperature_input',      'ºC',               0,      2   ],
  'integral2_curve_slope'        : ['r3d', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_min'          : ['r3e', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_max'          : ['r3f', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_target'       : ['r40', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_actual'       : ['r41', 'temperature_input',      'ºC',               0,    200   ],
  'outdoor_stop_t'               : ['r42', 'temperature_input',      'ºC',               0,    100   ],
  'preassure_pipe_limit_t'       : ['r43', 'temperature_input',      'ºC',               0,    200   ],
  'hotwater_start_t'             : ['r44', 'temperature_input',      'ºC',               0,    100   ],
  'hotwater_runtime_m'           : ['r45', 'time_input',             'min',               0,  32767   ],
  'heatpump_runtime_m'           : ['r46', 'time_input',             'min',               0,  32767   ],
  'legionella_runtime_m'         : ['r47', 'time_input',             'days',              0,  32767   ],
  'legionella_stop_t'            : ['r48', 'temperature_input',      'ºC',               0,    100   ],
  'integral1_a_limit'            : ['r49', 'sensor_input',           'Cmin',         -32768,  32767   ],
  'integral1_hysteresis_t'       : ['r4a', 'temperature_input',      'ºC',               0,    100   ],
  'returnline_max_t'             : ['r4b', 'temperature_input',      'ºC',               0,    100   ],
  'start_interval_min_m'         : ['r4c', 'time_input',             'min',               0,  32767   ],
  'brine_min_t'                  : ['r4d', 'temperature_input',      'ºC',             -25,    100   ],
  'cooling_target_t'             : ['r4e', 'temperature_input',      'ºC',               0,     50   ],
  'integral2_a_limit'            : ['r4f', 'sensor_input',           '10 Cmin',           0,    200   ],
  'integral2_hysteresis_t'       : ['r50', 'temperature_input',      'ºC',               0,    100   ],
  'elect_boiler_steps_max'       : ['r51', 'sensor_input',           'steps',        -32768,  32767   ],
  'current_consumption_max_a'    : ['r52', 'sensor_input',           'A',            -32768,  32767   ],
  'shunt_time_s'                 : ['r53', 'time_input',             's',                 0,  32767   ],
  'hotwater_stop_t'              : ['r54', 'temperature_input',      'ºC',               0,    100   ],
  'manual_test_mode_on'          : ['r55', 'sensor',                 'mode',                          ],
  'status7'                      : ['r56', 'sensor',                 '',                              ],
  'language'                     : ['r57', 'sensor_language',        'language',                      ],
  'status8'                      : ['r58', 'sensor',                 '',                              ],
  'factory_reset_req'            : ['r59', 'sensor',                 'setting',                       ],
  'runtime_counters_reset_req'   : ['r5a', 'sensor_boolean',         'Boolean',                       ],
  'outdoor_sensor_offset_t'      : ['r5b', 'temperature',            'ºC',                           ],
  'supplyline_sensor_offset_t'   : ['r5c', 'temperature',            'ºC',                           ],
  'returnline_sensor_offset_t'   : ['r5d', 'temperature',            'ºC',                           ],
  'boiler_sensor_offset_t'       : ['r5e', 'temperature',            'ºC',                           ],
  'brine_in_sensor_offset_t'     : ['r5f', 'temperature',            'ºC',                           ],
  'brine_out_sensor_offset_t'    : ['r60', 'temperature',            'ºC',                           ],
  'heatingsystem_type'           : ['r61', 'sensor',                 'type',                          ],
  'opt_phasemeassure_installed'  : ['r62', 'binary_sensor',          'type',         0x0001           ],
  'opt_2_installed'              : ['r62', 'binary_sensor',          'type',         0x0002           ],
  'opt_hgw_installed'            : ['r62', 'binary_sensor',          'type',         0x0004           ],
  'opt_4_installed'              : ['r62', 'binary_sensor',          'type',         0x0008           ],
  'opt_5_installed'              : ['r62', 'binary_sensor',          'type',         0x0010           ],
  'opt_6_installed'              : ['r62', 'binary_sensor',          'type',         0x0020           ],
  'opt_optimum_installed'        : ['r62', 'binary_sensor',          'type',         0x0040           ],
  'opt_flowguard_installed'      : ['r62', 'binary_sensor',          'type',         0x0080           ],
  'internal_logging_t'           : ['r63', 'time',                   'min',                           ],
  'brine_runout_t'               : ['r64', 'time',                   '*10s',                          ],
  'brine_run_in'                 : ['r65', 'time',                   '*10s',                          ],
  'legionella_run_on'            : ['r66', 'sensor_boolean',         'Boolean',                       ],
  'legionell_run_length_h'       : ['r67', 'time',                   'h',                             ],
  'compressor_runtime_h'         : ['r68', 'time',                   'h',                             ],
  'msd1_dvp'                     : ['r69', 'sensor',                 '',                              ],
  'boiler_3kw_runtime_h'         : ['r6a', 'time',                   'h',                             ],
  'msd1_dtp'                     : ['r6b', 'sensor',                 '',                              ],
  'hotwater_runtime_h'           : ['r6c', 'time',                   'h',                             ],
  'msd1_dvv'                     : ['r6d', 'sensor',                 '',                              ],
  'passive_cooling_runtime_h'    : ['r6e', 'time',                   'h',                             ],
  'msd1_d'                       : ['r6f', 'sensor',                 '',                              ],
  'active_cooling_runtime_h'     : ['r70', 'time',                   'h',                             ],
  'msd1_d'                       : ['r71', 'sensor',                 '',                              ],
  'boiler_6kw_on_runtime_h'      : ['r72', 'time',                   'h',                             ],
  'msd1_d'                       : ['r73', 'sensor',                 '',                              ],
  'graph_display_offset'         : ['r74', 'sensor',                 '',                              ],
  'room_sensor_set_t'            : ['rf0', 'temperature',            'ºC',               0,     50   ],
  'time'                         : ['rf0', 'time',                   's',                 0,     50   ],

}

# Translation dictionary
id_names = {  
  'outdoor_t'                    : 'Outdoor temp.',
  'indoor_t'                     : 'Indoor temp.',
  'indoor_dec_t'                 : 'Indoor temp., decimal',
  'indoor_target_t'              : 'Indoor target temp.',
  'indoor_target_dec_t'          : 'Indoor target temp., decimal',
  'supplyline_t'                 : 'Supplyline temp.',
  'returnline_t'                 : 'Returnline temp.',
  'boiler_t'                     : 'Hotwater temp.',
  'brine_out_t'                  : 'Brine out temp.',
  'brine_in_t'                   : 'Brine in temp.',
  'cooling_t'                    : 'Cooling temp.',
  'supply_shunt_t'               : 'Supplyline temp., shunt',
  'current_consumed_a'           : 'Electrical Current',
  'boiler_3kw_on'                : 'Aux. heater 3 kW',
  'boiler_6kw_on'                : 'Aux. heater 6 kW',
  'supplyline_target_t'          : 'Supplyline target temp.',
  'supplyline_shunt_target_t'    : 'Supplyline target temp., shunt',
  'brine_pump_on'                : 'Brinepump',
  'compressor_on'                : 'Compressor',
  'supply_pump_on'               : 'Flowlinepump',
  'hotwaterproduction_on'        : 'Hotwater production.',
  'aux2_heating_on'              : 'Auxilliary 2',
  'shunt1_n'                     : 'Shunt -',
  'shunt1_p'                     : 'Shunt +',
  'aux1_heating_on'              : 'Auxilliary 1',
  'shunt2_n'                     : 'Shuntgroup -',
  'shunt2_p'                     : 'Shuntgroup +',
  'shount_cooling_n'             : 'Shunt cooling -',
  'shount_cooling_p'             : 'Shunt cooling +',
  'active_cooling_on'            : 'Active cooling',
  'passive_cooling_on'           : 'Passive cooling',
  'alarm_indication_on'          : 'Alarm',
  'pwm_out_period'               : 'PWM Out',
  'highpreassure_alm'            : 'Alarm highpr.pressostate',
  'lowpreassure_alm'             : 'Alarm lowpr.pressostate',
  'motorbreaker_alm'             : 'Alarm motorcircuit breaker',
  'brine_flow_alm'               : 'Alarm low flow brine',
  'bine_temperature_alm'         : 'Alarm low temp. brine',
  'outdoor_sensor_alm'           : 'Alarm outdoor t-sensor',
  'supplyline_sensor_alm'        : 'Alarm supplyline t-sensor',
  'returnline_sensor_alm'        : 'Alarm returnline t-sensor',
  'boiler_sensor_alm'            : 'Alarm hotw. t-sensor',
  'indoor_sensor_alm'            : 'Alarm indoor t-sensor',
  'phase_order_alm'              : 'Alarm incorrect 3-phase order',
  'overheating_alm'              : 'Alarm overheating',
  'demand1'                      : 'DEMAND1',
  'demand2'                      : 'DEMAND2',
  'pressurepipe_t'               : 'Pressurepipe temp.',
  'hgw_water_t'                  : 'Hotw. supplyline temp.',
  'integral1'                    : 'Integral',
  'integral1_a_limit'            : 'Integral, reached A-limit',
  'defrost_time_m'               : 'Defrost',
  'time_to_start_min_m'          : 'Minimum time to start',
  'sw_version'                   : 'Program version',
  'supply_pump_speed'            : 'Flowlinepump speed',
  'brine_pump_speed'             : 'Brinepump speed',
  'status3_m'                    : 'STATUS3',
  'indoor_requested_t'           : 'Indoor target temp.',
  'main_mode'                    : 'Mode',
  'integral1_curve_slope'        : 'Curve',
  'integral1_curve_min'          : 'Curve min',
  'integral1_curve_max'          : 'Curve max',
  'integral1_curve_p5'           : 'Curve +5',
  'integral1_curve_0'            : 'Curve 0',
  'integral1_curve_n5'           : 'Curve -5',
  'heating_stop_t'               : 'Heatstop',
  'reduction_t'                  : 'Temp. reduction',
  'room_factor'                  : 'Room factor',
  'integral2_curve_slope'        : 'Curve 2',
  'integral2_curve_min'          : 'Curve 2 min',
  'integral2_curve_max'          : 'Curve 2 max',
  'integral2_curve_target'       : 'Curve 2, Target',
  'integral2_curve_actual'       : 'Curve 2, Actual',
  'outdoor_stop_t'               : 'Outdoor stop temp. (20=-20C)',
  'preassure_pipe_limit_t'       : 'Pressurepipe, temp. limit',
  'hotwater_start_t'             : 'Hotwater starttemp.',
  'hotwater_runtime_m'           : 'Hotwater operating time',
  'heatpump_runtime_m'           : 'Heatpump operating time',
  'legionella_runtime_m'         : 'Legionella interval',
  'legionella_stop_t'            : 'Legionella stop temp.',
  'integral1_a_limit'            : 'Integral limit A1',
  'integral1_hysteresis_t'       : 'Hysteresis, heatpump',
  'returnline_max_t'             : 'Returnline temp., max limit',
  'start_interval_min_m'         : 'Minimum starting interval',
  'brine_min_t'                  : 'Brinetemp., min limit (-15=OFFV)',
  'cooling_target_t'             : 'Cooling, target',
  'integral2_a_limit'            : 'Integral limit A2',
  'integral2_hysteresis_t'       : 'Hysteresis limit, aux',
  'elect_boiler_steps_max'       : 'Max step, aux',
  'current_consumption_max_a'    : 'Electrical current, max limit',
  'shunt_time_s'                 : 'Shunt time',
  'hotwater_stop_t'              : 'Hotwater stop temp.',
  'manual_test_mode_on'          : 'Manual test mode',
  'status7'                      : 'DT_LARMOFF',
  'language'                     : 'Language',
  'status8'                      : 'SERVFAS',
  'factory_reset_req'            : 'Factory settings',
  'runtime_counters_reset_req'   : 'Reset runtime counters',
  'outdoor_sensor_offset_t'      : 'Calibration outdoor sensor',
  'supplyline_sensor_offset_t'   : 'Calibration supplyline sensor',
  'returnline_sensor_offset_t'   : 'Calibration returnline sensor',
  'boiler_sensor_offset_t'       : 'Calibration hotwater sensor',
  'brine_in_sensor_offset_t'     : 'Calibration brine out sensor',
  'brine_out_sensor_offset_t'    : 'Calibration brine in sensor',
  'heatingsystem_type'           : 'Heating system type 0=VL 4=D',
  'opt_phasemeassure_installed'  : 'Add-on phase order measurement',
  'opt_2_installed'              : 'TILL2',
  'opt_hgw_installed'            : 'Add-on HGW',
  'opt_4_installed'              : 'TILL4',
  'opt_5_installed'              : 'TILL5',
  'opt_6_installed'              : 'TILL6',
  'opt_optimum_installed'        : 'Add-on Optimum',
  'opt_flowguard_installed'      : 'Add-on flow guard',
  'internal_logging_t'           : 'Logging time',
  'brine_runout_t'               : 'Brine run-out duration',
  'brine_run_in'                 : 'Brine run-in duration',
  'legionella_run_on'            : 'Legionella peak heating enable',
  'legionell_run_length_h'       : 'Legionella peak heating duration',
  'compressor_runtime_h'         : 'Runtime compressor',
  'msd1_dvp'                     : 'DVP_MSD1',
  'boiler_3kw_runtime_h'         : 'Runtime 3 kW',
  'msd1_dtp'                     : 'DTS_MSD1',
  'hotwater_runtime_h'           : 'Runtime hotwater production',
  'msd1_dvv'                     : 'DVV_MSD1',
  'passive_cooling_runtime_h'    : 'Runtime passive cooling',
  'msd1_d'                       : 'DPAS_MSD1',
  'active_cooling_runtime_h'     : 'Runtime active cooling',
  'msd1_d'                       : 'DACT_MSD1',
  'boiler_6kw_on_runtime_h'      : 'Runtime 6 kW',
  'msd1_d'                       : 'DTS2_MSD1',
  'graph_display_offset'         : 'GrafCounterOffSet   ',
  'room_sensor_set_t'            : 'Room sensor, Set',


}
# Unit dictionary
id_units = {  
  'outdoor_t'                    : 'ºC',
  'indoor_t'                     : 'ºC',
  'indoor_dec_t'                 : '0.1C',
  'indoor_target_t'              : 'ºC',
  'indoor_target_dec_t'          : '0.1C',
  'supplyline_t'                 : 'ºC',
  'returnline_t'                 : 'ºC',
  'boiler_t'                     : 'ºC',
  'brine_out_t'                  : 'ºC',
  'brine_in_t'                   : 'ºC',
  'cooling_t'                    : 'ºC',
  'supply_shunt_t'               : 'ºC',
  'current_consumed_a'           : 'A',
  'boiler_3kw_on'                : 'Boolean',
  'boiler_6kw_on'                : 'Boolean',
  'supplyline_target_t'          : 'ºC',
  'supplyline_shunt_target_t'    : 'ºC',
  'brine_pump_on'                : 'Boolean',
  'compressor_on'                : 'Boolean',
  'supply_pump_on'               : 'Boolean',
  'hotwaterproduction_on'        : 'Boolean',
  'aux2_heating_on'              : 'Boolean',
  'shunt1_n'                     : 'Boolean',
  'shunt1_p'                     : 'Boolean',
  'aux1_heating_on'              : 'Boolean',
  'shunt2_n'                     : 'Boolean',
  'shunt2_p'                     : 'Boolean',
  'shount_cooling_n'             : 'Boolean',
  'shount_cooling_p'             : 'Boolean',
  'active_cooling_on'            : 'Boolean',
  'passive_cooling_on'           : 'Boolean',
  'alarm_indication_on'          : 'Boolean',
  'pwm_out_period'               : '%',
  'highpreassure_alm'            : 'Boolean',
  'lowpreassure_alm'             : 'Boolean',
  'motorbreaker_alm'             : 'Boolean',
  'brine_flow_alm'               : 'Boolean',
  'bine_temperature_alm'         : 'Boolean',
  'outdoor_sensor_alm'           : 'Boolean',
  'supplyline_sensor_alm'        : 'Boolean',
  'returnline_sensor_alm'        : 'Boolean',
  'boiler_sensor_alm'            : 'Boolean',
  'indoor_sensor_alm'            : 'Boolean',
  'phase_order_alm'              : 'Boolean',
  'overheating_alm'              : 'Boolean',
  'demand1'                      : '  ',
  'demand2'                      : '  ',
  'pressurepipe_t'               : 'ºC',
  'hgw_water_t'                  : 'ºC',
  'integral1'                    : 'C*min',
  'integral1_a_limit'            : '  ',
  'defrost_time_m'               : '*10s',
  'time_to_start_min_m'          : 'min',
  'sw_version'                   : '  ',
  'supply_pump_speed'            : '%',
  'brine_pump_speed'             : '%',
  'status3_m'                    : '  ',
  'indoor_requested_t'           : 'ºC',
  'main_mode'                    : 'läge #',
  'integral1_curve_slope'        : 'ºC',
  'integral1_curve_min'          : 'ºC',
  'integral1_curve_max'          : 'ºC',
  'integral1_curve_p5'           : 'ºC',
  'integral1_curve_0'            : 'ºC',
  'integral1_curve_n5'           : 'ºC',
  'heating_stop_t'               : 'ºC',
  'reduction_t'                  : 'ºC',
  'room_factor'                  : 'ºC',
  'integral2_curve_slope'        : 'ºC',
  'integral2_curve_min'          : 'ºC',
  'integral2_curve_max'          : 'ºC',
  'integral2_curve_target'       : 'ºC',
  'integral2_curve_actual'       : 'ºC',
  'outdoor_stop_t'               : 'ºC',
  'preassure_pipe_limit_t'       : 'ºC',
  'hotwater_start_t'             : 'ºC',
  'hotwater_runtime_m'           : 'min',
  'heatpump_runtime_m'           : 'min',
  'legionella_runtime_m'         : 'days',
  'legionella_stop_t'            : 'ºC',
  'integral1_a_limit'            : 'C*min',
  'integral1_hysteresis_t'       : 'ºC',
  'returnline_max_t'             : 'ºC',
  'start_interval_min_m'         : 'min',
  'brine_min_t'                  : 'ºC',
  'cooling_target_t'             : 'ºC',
  'integral2_a_limit'            : '10 C*min',
  'integral2_hysteresis_t'       : 'ºC',
  'elect_boiler_steps_max'       : '# steps',
  'current_consumption_max_a'    : 'A',
  'shunt_time_s'                 : 's',
  'hotwater_stop_t'              : 'ºC',
  'manual_test_mode_on'          : 'mode #',
  'status7'                      : '  ',
  'language'                     : 'language #',
  'status8'                      : '  ',
  'factory_reset_req'            : 'setting #',
  'runtime_counters_reset_req'   : 'Boolean',
  'outdoor_sensor_offset_t'      : 'ºC',
  'supplyline_sensor_offset_t'   : 'ºC',
  'returnline_sensor_offset_t'   : 'ºC',
  'boiler_sensor_offset_t'       : 'ºC',
  'brine_in_sensor_offset_t'     : 'ºC',
  'brine_out_sensor_offset_t'    : 'ºC',
  'heatingsystem_type'           : 'type #',
  'opt_phasemeassure_installed'  : 'Boolean',
  'opt_2_installed'              : 'Boolean',
  'opt_hgw_installed'            : 'Boolean',
  'opt_4_installed'              : 'Boolean',
  'opt_5_installed'              : 'Boolean',
  'opt_6_installed'              : 'Boolean',
  'opt_optimum_installed'        : 'Boolean',
  'opt_flowguard_installed'      : 'Boolean',
  'internal_logging_t'           : 'min',
  'brine_runout_t'               : '10 s',
  'brine_run_in'                 : '10 s',
  'legionella_run_on'            : 'Boolean',
  'legionell_run_length_h'       : 'h',
  'compressor_runtime_h'         : 'h',
  'msd1_dvp'                     : '  ',
  'boiler_3kw_runtime_h'         : 'h',
  'msd1_dtp'                     : '  ',
  'hotwater_runtime_h'           : 'h',
  'msd1_dvv'                     : '  ',
  'passive_cooling_runtime_h'    : 'h',
  'msd1_d'                       : '  ',
  'active_cooling_runtime_h'     : 'h',
  'msd1_d'                       : '  ',
  'boiler_6kw_on_runtime_h'      : 'h',
  'msd1_d'                       : '  ',
  'graph_display_offset'         : '  ',
  'room_sensor_set_t'            : 'ºC',

}
