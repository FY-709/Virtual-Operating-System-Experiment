using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using OpService.Models;
using RabbitMQ.Client;

namespace OpService.Controllers
{

    [ApiController]
    [Route("api")]
    public class CodeController : Controller
    {
        private readonly CodeContext _context;
        private readonly ILogger<CodeController> _logger;

        public CodeController(CodeContext context, ILogger<CodeController> logger)
        {
            _context = context;
            _logger = logger;
        }

        [HttpPost("putCode")]
        public ActionResult<Info> PutCode([FromBody] PutCode codes)
        {
            var factory = new ConnectionFactory() { HostName = "localhost" };
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    // channel.QueueDeclare(queue: "test", durable: true, autoDelete: false);
                    string message = codes.id;

                    message += codes.code;
                    var body = Encoding.UTF8.GetBytes(message);
                    channel.BasicPublish(exchange: "", routingKey: "test", body: body);
                    Console.WriteLine("[x] send {0}", message);

                }
            }
            Dictionary<string, string> response = new Dictionary<string, string>();
            response.Add("info", "success");
            _logger.LogInformation("Message displayed: {Message}", response.ToString());
            var m = new Info();
            m.i_status = "success";
           return m;
        }

        [HttpPost("getCodeStatus")]
        public ActionResult<Object> GetCodeStatus(GetCode code){
            Console.WriteLine("[x] send {0}", code.id);
            var r = _context.cdata.Where(c => c.c_id == code.id).ToList();
            if(r.Count != 0){
                return r[0];
            }
            else{
                var m = new Info();
                m.i_status = "false";
                return m;
            }
        }


        [HttpGet("test")]
        public ActionResult<string> GetTest()
        {
            return "test";
        }

    }

}